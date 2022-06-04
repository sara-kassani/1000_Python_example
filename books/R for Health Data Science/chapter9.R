
# Logistic regression -----------------------------------------------------

# Generalized linear modelling is an extension to the linear modelling. It allows the principles of linear regression to be applied
# when outcomes are not continuous numeric variables.


### Data preparation and exploratory analysis -------------------------------
library(tidyverse)
library(finalfit)

melanoma <- boot::melanoma

melanoma %>% glimpse()
melanoma %>% ff_glimpse()


### Recode the data ---------------------------------------------------------
melanoma <- melanoma %>% 
  mutate(sex.factor = factor(sex) %>%
           fct_recode("Female" = "0",
                      "Male" = "1") %>%
           ff_label("Sex"),
         
         ulcer.factor = factor(ulcer) %>%
           fct_recode("Present" = "1",
                      "Absent" = "0") %>%
           ff_label("Ulcerated tumour"),
         
         age = ff_label(age, "Age (years)"),
         
         year = ff_label(year, "Year"),
         
         status.factor = factor(status) %>%
           fct_recode("Died melanoma" = "1",
                      "Alive" = "2",
                      "Died - other" = "3") %>%
           fct_relevel("Alive") %>%
           
           ff_label("Status"),
         t_stage.factor =
           thickness %>%
           cut(breaks = c(0, 1.0, 2.0, 4.0,
                          max(thickness, na.rm=TRUE)),
               include.lowest = TRUE)
  )

# Check the cut() function has worked:

melanoma$t_stage.factor %>% levels()
# [1] "[0,1]"    "(1,2]"    "(2,4]"    "(4,17.4]"

# Recode for ease.
melanoma <- melanoma %>%
  mutate(
    t_stage.factor =
      fct_recode(t_stage.factor,
                 "T1" = "[0,1]",
                 "T2" = "(1,2]",
                 "T3" = "(2,4]",
                 "T4" = "(4,17.4]") %>%
      ff_label("T-stage")
  )

# histogram of time stratified by status.factor
library(ggplot2)
melanoma %>% 
  ggplot(aes(x= time / 365)) +
  geom_histogram() +
  facet_grid( . ~ status.factor) + 
  ggtitle('Time to outcome/follow-up times for patients in the melanoma dataset.')


# Let’s decide then to look at 5-year mortality from melanoma. The deànition of this will be at 5 years after surgery, who had 
# died from melanoma and who had not.

# 5-year mortality
melanoma <- melanoma %>% 
  mutate(
    mort_5yr =
      if_else((time/365)<5 &
                (status == 1),
              "Yes", # then
              "No") %>% # else
      fct_relevel("No") %>%
      ff_label("5-year survival")
  )

# Plot the data
# We are interested in the association between tumour ulceration and outcomes

p1 <- melanoma %>%
  ggplot(aes(x = ulcer.factor, fill = mort_5yr)) +
  geom_bar() +
  theme(legend.position = "none")

p2 <- melanoma %>%
  ggplot(aes(x = ulcer.factor, fill = mort_5yr)) +
  geom_bar(position = "fill") +
  ylab("proportion")

library(patchwork)
p1 + p2


# As we might have anticipated from our work in the previous chapter, 5-year mortality is higher in patients with ulcerated tumours compared with those with non-ulcerated tumours.
# 
# We are also interested in other variables that may be associated with tumour ulceration. If they are also associated with our outcome, then they will confound the estimate of the direct effect of tumour ulceration. We can plot out these relationships, or tabulate them instead.



# Tabulate data -----------------------------------------------------------

# We will use the convenient summary_factorlist() function from the finalfit package to look for differences across other variables by tumour ulceration.

library(finalfit)
dependent <- "ulcer.factor"
explanatory <- c("age", "sex.factor", "year", "t_stage.factor")
melanoma %>%
  summary_factorlist(dependent, explanatory, p = TRUE, add_dependent_label = TRUE)

# It appears that patients with ulcerated tumours were older, more likely to be male, and had thicker/higher stage tumours. 
# It is important therefore to consider inclusion of these variables in a regression model.


# Linearity of continuous variables to the response -----------------------

# A graphical check of linearity can be performed using a best àt “loess” line. 
# This is on the probability scale, so it is not going to be straight. But it should be monotonic - it should only ever go up or down.


melanoma %>%
  mutate(
    mort_5yr.num = as.numeric(mort_5yr) - 1) %>%
  select(mort_5yr.num, age, year) %>%
  pivot_longer(all_of(c("age", "year")), names_to = "predictors") %>%
  ggplot(aes(x = value, y = mort_5yr.num)) +
  geom_point(size = 0.5, alpha = 0.5) +
  geom_smooth(method = "loess") +
  facet_wrap(~predictors, scales = "free_x") +
  ggtitle('Linearity of our continuous explanatory variables to the outcome (5-year mortality).')

# This plot shows that age is interesting as the relationship is u-shaped. The chance of death is higher in the young and 
# the old compared with the middle-aged. 
# This will need to be accounted for in any model including age as a predictor.


# Multicollinearity -------------------------------------------------------

# The ggpairs() function from library(GGally) is a good way of svisualising all two-way associations

library(GGally)
explanatory <- c("ulcer.factor", "age", "sex.factor", "year", "t_stage.factor")
melanoma %>%
  remove_labels() %>% # ggpairs doesn't work well with labels
  ggpairs(columns = explanatory)


# 
# If you have many variables you want to check you can split them up.

# - Continuous to continuous
# Here we’re using the same library(GGally) code as above, but shortlisting the two categorical variables: age and year
# 

select_explanatory <- c("age", "year")
melanoma %>%
  remove_labels() %>%
  ggpairs(columns = select_explanatory)



#  - Continuous to categorical
# Let’s use a clever pivot_longer() and facet_wrap() combination to efficiently plot multiple variables against each other without using ggpairs(). 
# We want to compare everything against, for example, age so we need to include -age in the pivot_longer() call so it doesn’t get lumped up with everything else.

select_explanatory <- c("age", "ulcer.factor", "sex.factor", "t_stage.factor")
melanoma %>%
  select(all_of(select_explanatory)) %>%
  pivot_longer(-age) %>% # pivots all but age into two columns: name and value
  ggplot(aes(value, age)) +
  geom_boxplot() +
  facet_wrap(~name, scale = "free", ncol = 3) +
  coord_flip()

# Categorical to categorical

select_explanatory <- c("ulcer.factor", "sex.factor", "t_stage.factor")
melanoma %>%
  select(one_of(select_explanatory)) %>%
  pivot_longer(-sex.factor) %>%
  ggplot(aes(value, fill = sex.factor)) +
  geom_bar(position = "fill") +
  ylab("proportion") +
  facet_wrap(~name, scale = "free", ncol = 2) +
  coord_flip()


# None of the explanatory variables are highly correlated with one another.
# Variance ináation factor

dependent <- "mort_5yr"
explanatory <- c("ulcer.factor", "age", "sex.factor", "year", "t_stage.factor")
melanoma %>%
  glmmulti(dependent, explanatory) %>%
  car::vif()


# Fitting logistic regression models in base R ----------------------------

# The glm() stands for generalised linear model and is the standard base R approach to logistic regression.
# The glm() function has several options and many different types of model can be run. For instance, ‘Poisson regression’ for count data.
# 
# To run binary logistic regression use family = binomial. This defaults to family = binomial(link = ). 
# Other link functions exist, such as the probit function, but this makes little difference to ànal conclusions.
# Let’s start with a simple univariable model using the classical R approach.

fit1 <- glm(mort_5yr ~ ulcer.factor, data = melanoma, family = binomial)
summary(fit1)


coef(fit1) %>% exp()

confint(fit1) %>% exp()

# Note that the 95% conàdence interval is between the 2.5% and 97.5% quantiles of the distribution, hence why the results appear in this way.
# A good alternative is the tidy() function from the broom package.

library(broom)
fit1 %>%
  tidy(conf.int = TRUE, exp = TRUE)


# We can see from these results that there is a strong association between tumour ulceration and 5-year mortality (OR 6.68, 95%CI 3.18, 15.18).
# Model metrics can be extracted using the glance() function.

fit1 %>%
  glance()


# Modelling strategy for binary outcomes ----------------------------------



# Fitting logistic regression models with finalfit ------------------------

library(finalfit)
dependent <- "mort_5yr"
explanatory <- "ulcer.factor"
melanoma %>%
  finalfit(dependent, explanatory, metrics = TRUE)



# Criterion-based model fitting -------------------------------------------


# Model fitting -----------------------------------------------------------

library(finalfit)
dependent <- "mort_5yr"
explanatory <- c("ulcer.factor", "age", "sex.factor", "t_stage.factor")
fit2 = melanoma %>%
  finalfit(dependent, explanatory, metrics = TRUE)



melanoma <- melanoma %>%
  mutate(
    age.factor = cut(age,
                     breaks = c(0, 25, 50, 75, 100)) %>%
      ff_label("Age (years)"))

# Add this to relevel:
# fct_relevel("(50,75]")
melanoma %>%
  finalfit(dependent, c("ulcer.factor", "age.factor"), metrics = TRUE)

# There is no strong relationship between the categorical representation of age and the outcome. Let’s try a quadratic term.
# In base R, a quadratic term is added like this.

glm(mort_5yr ~ ulcer.factor +I(age^2) + age, data = melanoma, family = binomial) %>%
  summary()

# It can be done in Finalfit in a similar manner. Note with default univariable model settings, the quadratic and linear terms are
# considered in separate models, which doesn’t make much sense.

library(finalfit)
dependent <- "mort_5yr"
explanatory <- c("ulcer.factor", "I(age^2)", "age")
melanoma %>%
  finalfit(dependent, explanatory, metrics = TRUE)


# 
# The AIC is worse when adding age either as a factor or with a quadratic term to the base model.
# 
# One ànal method to visualise the contribution of a particular variable is to remove it from the full model. This is convenient in
# Finalfit.

library(finalfit)
dependent <- "mort_5yr"
explanatory <- c("ulcer.factor", "age.factor", "sex.factor", "t_stage.factor")
explanatory_multi <- c("ulcer.factor", "sex.factor", "t_stage.factor")
melanoma %>%
  finalfit(dependent, explanatory, explanatory_multi, keep_models = TRUE, metrics = TRUE)

# Now what about the variable sex. It has a significant association with the outcome in the univariable analysis, but much of this is
# explained by other variables in multivariable analysis. Is it contributing much to the model?

library(finalfit)
dependent <- "mort_5yr"
explanatory <- c("ulcer.factor", "sex.factor", "t_stage.factor")
explanatory_multi <- c("ulcer.factor", "t_stage.factor")

melanoma %>%
  finalfit(dependent, explanatory, explanatory_multi, keep_models = TRUE, metrics = TRUE)


library(finalfit)
dependent <- "mort_5yr"
explanatory <- c("ulcer.factor", "t_stage.factor")
explanatory_multi <- c("ulcer.factor*t_stage.factor")

melanoma %>%
  finalfit(dependent, explanatory, explanatory_multi, keep_models = TRUE, metrics = TRUE)


# There are no signiàcant interaction terms.
# Our ànal model table is therefore:


library(finalfit)
dependent <- "mort_5yr"
explanatory <- c("ulcer.factor", "age.factor", "sex.factor", "t_stage.factor")

explanatory_multi <- c("ulcer.factor", "t_stage.factor")
melanoma %>%
  finalfit(dependent, explanatory, explanatory_multi, metrics = TRUE)


# Odds ratio plot ---------------------------------------------------------

dependent <- "mort_5yr"
explanatory_multi <- c("ulcer.factor", "t_stage.factor")
melanoma %>%
  or_plot(dependent, explanatory_multi, breaks = c(0.5, 1, 2, 5, 10, 25),
          table_text_size = 3.5,
          title_text_size = 16)



# Correlated groups of observations ---------------------------------------

# Simulate data

# Simulate random hospital identifier
set.seed(1)
melanoma <- melanoma %>%
  mutate(hospital_id = sample(1:4, 205, replace = TRUE))
melanoma <- melanoma %>%
  mutate(hospital_id = c(rep(1:3, 50), rep(4, 55)))

# Plot the data


melanoma %>%
  mutate( mort_5yr.num = as.numeric(mort_5yr) - 1) %>% # Convert factor to 0 and 1
  ggplot(aes(x = as.numeric(t_stage.factor), y = mort_5yr.num)) +
  geom_jitter(width = 0.1, height = 0.1) +
  geom_smooth(method = 'loess', se = FALSE) +
  facet_wrap(~hospital_id) +
  labs(x= "T-stage", y = "Mortality (5 y)")



# Mixed effects models in base R ------------------------------------------

library(lme4)
melanoma %>%
  glmer(mort_5yr ~ t_stage.factor + (1 | hospital_id), data = ., family = "binomial") %>%
  summary()


# We find it more straightforward to use finalfit

dependent <- "mort_5yr"
explanatory <- "t_stage.factor"
random_effect <- "hospital_id"    #  Is the same as:
random_effect <- "(1 | hospital_id)"
melanoma %>%
  finalfit(dependent, explanatory, random_effect = random_effect, metrics = TRUE)


# We can incorporate our (made-up) hospital identifier into our final model from above. Using keep_models = TRUE, 
# we can compare univariable, multivariable and mixed effects models.

library(finalfit)
dependent <- "mort_5yr"
explanatory <- c("ulcer.factor", "age.factor", "sex.factor", "t_stage.factor")
explanatory_multi <- c("ulcer.factor", "t_stage.factor")
random_effect <- "hospital_id"
melanoma %>%
  finalfit(dependent, explanatory, explanatory_multi,
           random_effect,
           keep_models = TRUE,
           metrics = TRUE)




# Exercises -----------------------------------------------------------------------


# Investigate the association between sex and 5-year mortality for patients who have undergone surgery for melanoma.
# First recode the variables as shown in the text, then plot the counts and proportions for 5-year disease-specific mortality in women and men. 
# Is there an association between sex and mortality?
  
## Recode
melanoma <- melanoma %>%
  mutate(sex.factor = factor(sex) %>%
           fct_recode("Female" = "0",
                      "Male" = "1") %>%
           ff_label("Sex"),
         ulcer.factor = factor(ulcer) %>%
           fct_recode("Present" = "1",
                      "Absent" = "0") %>%
           ff_label("Ulcerated tumour"),
         age = ff_label(age, "Age (years)"),
         year = ff_label(year, "Year"),
         status.factor = factor(status) %>%
           fct_recode("Died melanoma" = "1",
                      "Alive" = "2",
                      "Died - other" = "3") %>%
           fct_relevel("Alive") %>%
           ff_label("Status"),
         t_stage.factor =
           thickness %>%
           cut(breaks = c(0, 1.0, 2.0, 4.0,
                          max(thickness, na.rm=TRUE)),
               include.lowest = TRUE)
  )

# Plot
p1 <- melanoma %>%
  ggplot(aes(x = sex.factor, fill = mort_5yr)) +
  geom_bar() +
  theme(legend.position = "none")
p2 <- melanoma %>%
  ggplot(aes(x = sex.factor, fill = mort_5yr)) +
  geom_bar(position = "fill") +
  ylab("proportion")

p1 + p2
  
# ----------------------------------------------------------------------------- 


# Make a table showing the relationship between sex and the variables age, Tstage and ulceration. Hint: summary_factorlist(). 
# Express age in terms of median and interquartile range. Include a statistical comparison. 
# What associations do you see?  
#   
  
  
## Recode T-stage first
melanoma <- melanoma %>%
  mutate(
    t_stage.factor =
      fct_recode(t_stage.factor,
                 T1 = "[0,1]",
                 T2 = "(1,2]",
                 T3 = "(2,4]",
                 T4 = "(4,17.4]") %>%
      ff_label("T-stage")
  )
dependent = "sex.factor"
explanatory = c("age", "t_stage.factor", "ulcer.factor")
melanoma %>%  
  
summary_factorlist(dependent, explanatory, p = TRUE,
                     na_include = TRUE,
                     cont = "median")
# Men have more T4 tumours and they are more likely to be ulcerated.

# ----------------------------------------------------------------------------- 



# Run a logistic regression model for 5-year disease-specific mortality including sex, age, T-stage and ulceration.
# What is the c-statistic for this model?
# Is there a relationship between sex and mortality, after adjustment for the other explanatory variables?
  
  
dependent = "mort_5yr"
explanatory = c("sex.factor", "age", "t_stage.factor", "ulcer.factor")
melanoma %>%
  finalfit(dependent, explanatory, metrics = TRUE)
# c-statistic = 0.798
# In multivariable model, male vs female OR 1.26 (0.57-2.76, p=0.558).
# No relationship after accounting for T-stage and tumour ulceration.
# Sex is confounded by these two variables.


 # ----------------------------------------------------------------------------- 
  
  # Make an odds ratio plot for this model.


dependent = "mort_5yr"
explanatory = c("sex.factor", "age", "t_stage.factor", "ulcer.factor")
melanoma %>%
  or_plot(dependent, explanatory)
