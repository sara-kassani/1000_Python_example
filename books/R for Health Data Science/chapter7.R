
# Linear regression -------------------------------------------------------

## load packages  -------------------------------------------------------

library(tidyverse)
library(gapminder)   #  the dataset
library(finalfit)
library(broom)
library(purrr)

theme_set(theme_bw())
gapdata <- gapminder

## check the data -------------------------------------------------------
glimpse(gapdata)
missing_glimpse(gapdata)
ff_glimpse(gapdata)    #  summary statistics for each variable

## plot the data --------------------------------------------------------

gapdata %>%  
  filter(continent == 'Europe') %>% 
  ggplot(aes(x= year, y= lifeExp)) + 
  geom_point() +
  facet_wrap(~ country) +
  scale_x_continuous(breaks= c(1960, 2000)) +
  geom_smooth(method= 'lm') + 
  ggtitle('Scatter plots with linear regression lines: Life expectancy by year in European countries')

# Simple linear regression ------------------------------------------------

# We can then investigate the intercepts and the slope coefficients (linear increase per year):
# First let’s plot two countries to compare, Turkey and United Kingdom

gapdata %>% 
  filter(country %in% c('Turkey', 'United Kingdom')) %>% 
  ggplot(aes(x= year, y= lifeExp, color= country)) +
  geom_point()


# First, let’s model the two countries separately.
# United Kingdom
fit_uk <- gapdata %>% 
  filter(country == 'United Kingdom') %>% 
  lm(lifeExp ~ year, data =.)

fit_uk %>% 
  summary()

          # Call:
          #   lm(formula = lifeExp ~ year, data = .)
          # 
          # Residuals:
          #   Min       1Q   Median       3Q      Max 
          # -0.69767 -0.31962  0.06642  0.36601  0.68165 
          # 
          # Coefficients:
          #   Estimate Std. Error t value Pr(>|t|)    
          # (Intercept) -2.942e+02  1.464e+01  -20.10 2.05e-09 ***
          #   year         1.860e-01  7.394e-03   25.15 2.26e-10 ***
          #   ---
          #   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
          # 
          # Residual standard error: 0.4421 on 10 degrees of freedom
          # Multiple R-squared:  0.9844,	Adjusted R-squared:  0.9829 
          # F-statistic: 632.5 on 1 and 10 DF,  p-value: 2.262e-10

# Turkey
fit_turkey <- gapdata %>% 
filter(country == 'Turkey') %>% 
  lm(lifeExp ~ year, data=.)

fit_turkey %>% 
  summary()


        # Call:
        #   lm(formula = lifeExp ~ year, data = .)
        # 
        # Residuals:
        #   Min      1Q  Median      3Q     Max 
        # -2.4373 -0.3457  0.1653  0.9008  1.1033 
        # 
        # Coefficients:
        #   Estimate Std. Error t value Pr(>|t|)    
        # (Intercept) -924.58989   37.97715  -24.35 3.12e-10 ***
        #   year           0.49724    0.01918   25.92 1.68e-10 ***
        #   ---
        #   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
        # 
        # Residual standard error: 1.147 on 10 degrees of freedom
        # Multiple R-squared:  0.9853,	Adjusted R-squared:  0.9839 
        # F-statistic: 671.8 on 1 and 10 DF,  p-value: 1.681e-10

# Accessing the coefàcients of linear regression
fit_uk$coefficients
fit_turkey$coefficients

      # > fit_uk$coefficients
      # (Intercept)         year 
      # -294.1965876    0.1859657 
      # > fit_turkey$coefficients
      # (Intercept)         year 
      # -924.5898865    0.4972399 

# A simple linear regression model will return two coefficients - the intercept and the slope (the second returned value).
# 
# The slopes make sense - the results of the linear regression say that in the UK, life expectancy increases by 0.186 every year,
# whereas in Turkey the change is 0.497 per year. The reason the intercepts are negative, however, may be less obvious.
# 
# In this example, the intercept is telling us that life expectancy at year 0 in the United Kingdom (some 2000 years ago) was -294 years. 
# While this is mathematically correct (based on the data we have), it obviously makes no sense in practice. 

# It is important to think about the range over which you can extend your model predictions, and where they just become unrealistic. 
# To make the intercepts meaningful, we will add in a new column called  year_from1952 and re-run fit_uk and fit_turkey using year_from1952 instead of year.

gapdata <- gapdata %>% 
  mutate(year_from1952 = year -1952)

fit_uk <- gapdata %>% 
  filter(country == 'United Kingdom') %>% 
  lm(lifeExp ~ year_from1952, data =.)

fit_turkey <- gapdata %>% 
  filter(country == 'Turkey') %>% 
  lm(lifeExp ~ year_from1952, data =.)

fit_uk$coefficients
fit_turkey$coefficients

            # > fit_uk$coefficients
            # (Intercept) year_from1952 
            # 68.8085256     0.1859657 
            # > fit_turkey$coefficients
            # (Intercept) year_from1952 
            # 46.0223205     0.4972399 


# Now, the updated results tell us that in year 1952, the life expectancy in the United Kingdom was 69 years. Note that the slopes do not change. 
# There was nothing wrong with the original model and the results were correct, the intercept was just not meaningful.


### Accessing all model information tidy() and glance() ---------------------

# We use the tidy() function from library(broom) to get the variable(s) and speciàc values in a nice tibble:

fit_uk %>% 
  tidy()

              # term          estimate std.error statistic  p.value
              # <chr>            <dbl>     <dbl>     <dbl>    <dbl>
              # 1 (Intercept)     68.8     0.240       287.  6.58e-21
              # 2 year_from1952    0.186   0.00739      25.1 2.26e-10

fit_turkey %>% 
  tidy()

            # term          estimate std.error statistic  p.value
            # <chr>            <dbl>     <dbl>     <dbl>    <dbl>
            # 1 (Intercept)     46.0      0.623       73.9 5.03e-15
            # 2 year_from1952    0.497    0.0192      25.9 1.68e-10


# And we use the glance() function to get overall model statistics (mostly  the r.squared)

fit_uk %>% 
  glance()

# r.squared adj.r.squared sigma statistic  p.value    df logLik   AIC   BIC deviance df.residual  nobs
#         <dbl>         <dbl> <dbl>     <dbl>    <dbl> <dbl>  <dbl> <dbl> <dbl>    <dbl>       <int> <int>
#   1     0.984         0.983 0.442      633. 2.26e-10     1  -6.14  18.3  19.7     1.95          10    12

fit_turkey %>% 
  glance()

# r.squared adj.r.squared sigma statistic  p.value    df logLik   AIC   BIC deviance df.residual  nobs
#         <dbl>         <dbl> <dbl>     <dbl>    <dbl> <dbl>  <dbl> <dbl> <dbl>    <dbl>       <int> <int>
#   1     0.985         0.984  1.15      672. 1.68e-10     1  -17.6  41.2  42.6     13.2          10    12



# Multivariable linear regression -----------------------------------------

# Multivariable linear regression includes more than one explanatory variable.
# There are a few ways to include more variables, depending on whether they should share the intercept and how they interact:
# Simple linear regression (exactly one predictor variable):
#         myfit = lm(lifeExp year, data = gapdata)
# Multivariable linear regression (additive):
#         myfit = lm(lifeExp year + country, data = gapdata)
# Multivariable linear regression (interaction):
#         myfit = lm(lifeExp year * country, data = gapdata)
# This equivalent to: myfit = lm(lifeExp year + country +
#                                  year:country, data = gapdata)

# These examples of multivariable regression include two variables: year and country, but we could include more by adding them with +,
# it does not just have to be two.


### Model 1: year only ------------------------------------------------------

# UK and Turkey dataset:
gapdata_UK_T <- gapdata %>% 
  filter(country %in% c('Turkey', 'United Kingdom'))

fit_both1 <- gapdata_UK_T %>% 
  lm(lifeExp ~ year_from1952, data =.)

fit_both1

# Call:
#   lm(formula = lifeExp ~ year_from1952, data = .)
# 
# Coefficients:
#   (Intercept)  year_from1952  
# 57.4154         0.3416  

gapdata_UK_T %>% 
  mutate(pred_lifeExp = predict(fit_both1)) %>% 
  ggplot() +
  geom_point(aes(x= year, y= lifeExp, color= country)) + 
  geom_line(aes(x= year, y= pred_lifeExp)) +
  ggtitle('Scatter and line plot. Life expectancy in Turkey and the UK - univariable fit.')


# By fitting to year only ( lifeExp year_from1952), the model ignores country. This gives us a fitted line which is the average of 
# life expectancy in the UK and Turkey. This may be desirable, depending on the question. But here we want to best describe the data.

# How we made the plot and what does predict() do? Previously, we were using geom_smooth(method = "lm") to conveniently add linear
# regression lines on a scatter plot. When a scatter plot includes categorical value (e.g.,  the points are coloured by a variable),
# the regression lines geom_smooth() draws are multiplicative. That is great, and almost always exactly what we want. 
# Here, however, to illustrate the difference between the different models, we will have to use the predict() model and geom_line() 
# to have full control over the plotted regression lines.

gapdata_UK_T %>% 
  mutate(pred_lifeExp = predict(fit_both1)) %>% 
  select(country, year, lifeExp, pred_lifeExp) %>% 
  group_by(country) %>% 
  slice(1, 6, 12)

# Note how the slice() function recognizes group ˙ by() and in this case shows us the 1st, 6th, and 12th observation within each group.


### Model 2: year + country -------------------------------------------------

fit_both2 <- gapdata_UK_T %>% 
  lm(lifeExp ~ year_from1952 + country, data =.)

fit_both2
  
                  # Call:
                  #   lm(formula = lifeExp ~ year_from1952 + country, data = .)
                  # 
                  # Coefficients:
                  #   (Intercept)          year_from1952  countryUnited Kingdom  
                  # 50.3023                 0.3416                14.2262  
          
gapdata_UK_T %>% 
  mutate(pred_lifeExp = predict(fit_both2)) %>% 
  ggplot() +
  geom_point(aes(x= year, y= lifeExp, color= country)) + 
  geom_line(aes(x= year, y= pred_lifeExp, color= country)) +
  ggtitle('Scatter and line plot. Life expectancy in Turkey and the UK - multivariable additive fit')


# This is better, by including country in the model, we now have fitted lines more closely representing the data. 
# However, the lines are constrained to be parallel. This is the additive model that was discussed above. 
# We need to include an interaction term to allow the effect of year on life expectancy to vary by country in a non-additive manner.


### Model 3: year * country -------------------------------------------------

fit_both3 <- gapdata_UK_T %>% 
  lm(lifeExp ~ year_from1952 * country, data =.)

fit_both3


# Call:
#   lm(formula = lifeExp ~ year_from1952 * country, data = .)
# 
# Coefficients:
#   (Intercept)                        year_from1952                countryUnited Kingdom  
#     46.0223                               0.4972                              22.7862  
# year_from1952:countryUnited Kingdom  
# -0.3113  

gapdata_UK_T %>% 
  mutate(pred_lifeExp= predict(fit_both3)) %>% 
  ggplot()+
  geom_point(aes(x= year, y= lifeExp, color= country)) +
  geom_line(aes(x= year, y= pred_lifeExp, color= country)) + 
  ggtitle('Scatter and line plot. Life expectancy in Turkey and the UK - multivariable multiplicative fit.')


# This fits the data much better than the previous two models. You can check the R-squared using summary(fit_both3).
# Advanced tip: we can apply a function on multiple objects at once by putting them in a list() and using a map_() function from 
# the purrr package. library(purrr) gets installed and loaded with library(tidyverse).


# you are starting to do similar things over and over again:

mod_stats1 <- glance(fit_both1)
mod_stats2 <- glance(fit_both2)
mod_stats3 <- glance(fit_both3)

# returns the exact same thing as:

library(purrr)
list(fit_both1, fit_both2, fit_both3) %>% 
  map_df(glance)

# r.squared adj.r.squared sigma statistic  p.value    df logLik   AIC   BIC deviance df.residual  nobs
# <dbl>         <dbl> <dbl>     <dbl>    <dbl> <dbl>  <dbl> <dbl> <dbl>    <dbl>       <int> <int>
# 1     0.373         0.344 7.98       13.1 1.53e- 3     1  -82.9 172.  175.    1403.           22    24
# 2     0.916         0.908 2.99      114.  5.18e-12     2  -58.8 126.  130.     188.           21    24
# 3     0.993         0.992 0.869     980.  7.30e-22     3  -28.5  67.0  72.9     15.1          20    24

# What happens here is that map_df() applies a function on each object in the list it gets passed, and returns a df (data frame). 
# In this case, the function is glance().


## Check assumptions -------------------------------------------------------

# The assumptions of linear regression can be checked with diagnostic plots, either by passing the fitted object (lm() output) to 
# base R plot(), or by using the more convenient function below.

install.packages('ggfortify')
library(ggfortify)
autoplot(fit_both3)    #  Diagnostic plots. Life expectancy in Turkey and the UK - multivariable multiplicative model


# Fitting more complex models ---------------------------------------------

# We will use The Western Collaborative Group Study dataset to explore the relationship between systolic blood pressure (sbp) and
# personality type (personality_2L), accounting for potential confounders such as weight ( weight).

### Reading from chapter 7.

# Get the data
wcgsdata <- finalfit::wcgs
wcgsdata

# plot the data
wcgsdata %>%
  ggplot(aes(x= weight, y= sbp, color= personality_2L)) +    # personality type 2
  geom_point(alpha= 0.2) +
  geom_smooth(method= 'lm', se= FALSE) +
  ggtitle('Scatter and line plot. Systolic blood pressure by weight and personality type.')

# From this plot, we can see that there is a weak relationship between weight and blood pressure.
# In addition, there is really no meaningful effect of personality type on blood pressure.


# Linear regression with finalfit -----------------------------------------

dependent <- 'sbp'
explanatory <- 'personality_2L'
fit_sbp1 <- wcgsdata %>% 
  finalfit(dependent, explanatory, metrics = TRUE)

fit_sbp1


                # [[1]]
                # Dependent: Systolic BP (mmHg)        unit        value    Coefficient (univariable)  Coefficient (multivariable)
                # Personality type B Mean (sd) 127.5 (14.4)                            -                            -
                #   A Mean (sd) 129.8 (15.7) 2.32 (1.26 to 3.37, p<0.001) 2.32 (1.26 to 3.37, p<0.001)
                # 
                # [[2]]
                # 
                # Number in data frame = 3154, Number in model = 3154, Missing = 0, Log-likelihood = -13031.39, AIC = 26068.8, R-squared = 0.0059, Adjusted R-squared = 0.0056



### read the explanation from chapter 7.

# Let’s now include subject weight, which we have hypothesized may influence blood pressure.

dependent <- 'sbp'
explanatory <- c('weight', 'personality_2L')

fit_sbp2 <- wcgsdata %>% 
  finalfit(dependent, explanatory, metrics = TRUE)

fit_sbp2


                # [[1]]
                # Dependent: Systolic BP (mmHg)                   unit        value    Coefficient (univariable)
                # Weight (pounds) [78.0,320.0] Mean (sd) 128.6 (15.1) 0.18 (0.16 to 0.21, p<0.001)
                # Personality type            B Mean (sd) 127.5 (14.4)                            -
                #   A Mean (sd) 129.8 (15.7) 2.32 (1.26 to 3.37, p<0.001)
                # Coefficient (multivariable)
                # 0.18 (0.16 to 0.20, p<0.001)
                # -
                #   1.99 (0.97 to 3.01, p<0.001)
                # 
                # [[2]]
                # 
                # Number in data frame = 3154, Number in model = 3154, Missing = 0, Log-likelihood = -12928.82, AIC = 25865.6, 
                # R-squared = 0.068, Adjusted R-squared = 0.068

# Let’s now add in other variables that may influence systolic blood pressure.

dependent <- 'sbp'
explanatory <- c('weight', 'personality_2L', 'age', 'height', 'chol', 'smoking')

fit_sbp3 <- wcgsdata %>% 
  finalfit(dependent, explanatory, metrics = TRUE)

fit_sbp3

# Let’s create a new variable called bmi, note the conversion from pounds and inches to kg and m:
wcgsdata <- wcgsdata %>% 
  mutate(bmi = ((weight * 0.4536) / (height * 0.0254)^2 ) %>% 
           ff_label('BMI'))


# Weight and height can now be replaced in the model with BMI.

explanatory = c('personality_2L', 'bmi', 'age', 'chol', 'smoking')

fit_sbp4 <- wcgsdata %>% 
  finalfit(dependent, explanatory, metrics = TRUE)

fit_sbp4

                                        # [[1]]
                                        # Dependent: Systolic BP (mmHg)                    unit        value     Coefficient (univariable)
                                        # Personality type             B Mean (sd) 127.5 (14.4)                             -
                                        #   A Mean (sd) 129.8 (15.7)  2.32 (1.26 to 3.37, p<0.001)
                                        # BMI   [11.2,39.0] Mean (sd) 128.6 (15.1)  1.69 (1.50 to 1.89, p<0.001)
                                        # Age (years)   [39.0,59.0] Mean (sd) 128.6 (15.1)  0.45 (0.36 to 0.55, p<0.001)
                                        # Cholesterol (mg/100 ml) [103.0,645.0] Mean (sd) 128.6 (15.1)  0.04 (0.03 to 0.05, p<0.001)
                                        # Smoking    Non-smoker Mean (sd) 128.6 (15.6)                             -
                                        #   Smoker Mean (sd) 128.7 (14.6) 0.08 (-0.98 to 1.14, p=0.883)
                                        # Coefficient (multivariable)
                                        # -
                                        #   1.51 (0.51 to 2.50, p=0.003)
                                        # 1.65 (1.46 to 1.85, p<0.001)
                                        # 0.41 (0.32 to 0.50, p<0.001)
                                        # 0.03 (0.02 to 0.04, p<0.001)
                                        # -
                                        #   0.98 (-0.03 to 1.98, p=0.057)
                                        # 
                                        # [[2]]
                                        # 
                                        # Number in dataframe = 3154, Number in model = 3142, Missing = 12, Log-likelihood = -12775.03, AIC = 25564.1, R-squared = 0.12, Adjusted R-squared = 0.12


# On the principle of parsimony, we may want to remove variables which are not contributing much to the model. 
# For instance, let’s compare models with and without the inclusion of smoking. This can be easily done using the finalfitexplanatory_multi option.

dependent <- 'sbp'
explanatory <- c('personality_2L', 'bmi', 'age', 'chol', 'smoking')
explanatory_multi <- c('personality_2L', 'bmi', 'age', 'chol')

fit_sbp5 <- wcgsdata %>% 
  finalfit(dependent, explanatory, explanatory_multi, keep_models = TRUE, metrics = TRUE)

fit_sbp5

                  # [[1]]
                  # Dependent: Systolic BP (mmHg)                    unit        value     Coefficient (univariable)
                  # Personality type             B Mean (sd) 127.5 (14.4)                             -
                  #   A Mean (sd) 129.8 (15.7)  2.32 (1.26 to 3.37, p<0.001)
                  # BMI   [11.2,39.0] Mean (sd) 128.6 (15.1)  1.69 (1.50 to 1.89, p<0.001)
                  # Age (years)   [39.0,59.0] Mean (sd) 128.6 (15.1)  0.45 (0.36 to 0.55, p<0.001)
                  # Cholesterol (mg/100 ml) [103.0,645.0] Mean (sd) 128.6 (15.1)  0.04 (0.03 to 0.05, p<0.001)
                  # Smoking    Non-smoker Mean (sd) 128.6 (15.6)                             -
                  #   Smoker Mean (sd) 128.7 (14.6) 0.08 (-0.98 to 1.14, p=0.883)
                  # Coefficient (multivariable) Coefficient (multivariable reduced)
                  # -                                   -
                  #   1.51 (0.51 to 2.50, p=0.003)        1.56 (0.57 to 2.56, p=0.002)
                  # 1.65 (1.46 to 1.85, p<0.001)        1.62 (1.43 to 1.82, p<0.001)
                  # 0.41 (0.32 to 0.50, p<0.001)        0.41 (0.32 to 0.50, p<0.001)
                  # 0.03 (0.02 to 0.04, p<0.001)        0.03 (0.02 to 0.04, p<0.001)
                  # -                                   -
                  #   0.98 (-0.03 to 1.98, p=0.057)                                   -
                  #   
                  #   [[2]]
                  # [[2]][[1]]
                  # [1] "Number in dataframe = 3154, Number in model = 3142, Missing = 12, Log-likelihood = -12775.03, AIC = 25564.1, R-squared = 0.12, Adjusted R-squared = 0.12"
                  # 
                  # [[2]][[2]]
                  # [1] "Number in dataframe = 3154, Number in model = 3142, Missing = 12, Log-likelihood = -12776.83, AIC = 25565.7, R-squared = 0.12, Adjusted R-squared = 0.12"

#--------------------------------------------------------------------------------------------

# We can also visualize models using plotting. This is useful for communicating a model in a restricted space, e.g., in a presentation.

fit_sbp5 <- wcgsdata %>% 
  ff_plot(dependent, explanatory_multi)


# We can check the assumptions as above.

dependent <- 'sbp'
explanatory_multi <- c('bmi', 'personality_2L', 'age', 'chol')


wcgsdata %>% 
  lmmulti(dependent, explanatory_multi) %>% 
  autoplot()


# An important message in the results relates to the highly significant pvalues in the table above. 
# Should we conclude that in a multivariable regression model controlling for BMI, age, and serum cholesterol, 
# blood pressure was significantly elevated in those with a Type A personality (1.56 (0.57 to 2.56, p=0.002) compared with Type B? 
# The p-value looks impressive, but the actual difference in blood pressure is only 1.6 mmHg. 
# Even at a population level, that may not be clinically significant, Fitting with our first thoughts when we saw the scatter plot.


# Exercises ---------------------------------------------------------------

# Plot the GDP per capita by year for countries in Europe. Add a best fit straight line to the plot. In which countries is the
# relationship not linear?
# Advanced: make the line curved by adding a quadratic/squared term, e.g., y x2 + x. Hint: check geom˙smooth() help page under formula.

gapdata %>% 
  filter(continent == 'Europe') %>% 
  ggplot(aes(x= year, y= gdpPercap)) +
  geom_point() +
  geom_smooth(method = 'lm') +
  facet_wrap(country ~ .)

# Countries not linear(Ireland, Montenegro, Serbia)
# Add quadratic term
gapdata %>% 
  filter(continent == 'Europe') %>% 
  ggplot(aes(x= year, y= gdpPercap)) +
  geom_point() +
  geom_smooth(method= 'lm', formula = 'y ~ poly(x, 2)') +
  facet_wrap(country ~ .)


# Compare the relationship between GDP per capita and year for two countries of your choice. If you can’t choose, make it Albania and Austria.
# Fit and plot a regression model that simply averages the values across the two countries.

# Fit and plot a best fit regression model. Use your model to determine the difference in GDP per capita for your countries in 1980.

# plot first
gapdata %>% 
  filter(country %in% c('Albania', 'Austria')) %>% 
  ggplot() +
  geom_point(aes(x= year, y= gdpPercap, color= country))


# fit average line between two countries
fit_both1 = gapdata %>% 
  filter(country %in% c('Albania', 'Austria')) %>% 
  lm(gdpPercap ~ year, data =.)

gapdata %>% 
  filter(country %in% c('Albania', 'Austria')) %>% 
  ggplot() +
  geom_point(aes(x= year, y= gdpPercap, color= country)) +
  geom_line(aes(x= year, y= predict(fit_both1)))



# Fit average line between two countries.
fit_both3 = gapdata %>%
  filter(country %in% c("Albania", "Austria")) %>%
  lm(gdpPercap ~ year * country, data = .)
gapdata %>%
  filter(country %in% c("Albania", "Austria")) %>%
  ggplot() +
  geom_point(aes(x = year, y = gdpPercap, colour = country)) +
  geom_line(aes(x = year, y = predict(fit_both3), group = country))


# You can use the regression equation by hand to work out the
difference
summary(fit_both3)
                            # Call:
                            #   lm(formula = gdpPercap ~ year * country, data = .)
                            # 
                            # Residuals:
                            #   Min       1Q   Median       3Q      Max 
                            # -1438.65  -194.08    42.83   416.81  1184.07 
                            # 
                            # Coefficients:
                            #   Estimate Std. Error t value Pr(>|t|)    
                            # (Intercept)         -104544.09   22069.11  -4.737 0.000126 ***
                            #   year                     54.46      11.15   4.885 8.96e-05 ***
                            #   countryAustria      -933229.89   31210.44 -29.901  < 2e-16 ***
                            #   year:countryAustria     480.11      15.77  30.452  < 2e-16 ***
                            #   ---
                            #   Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
                            # 
                            # Residual standard error: 666.6 on 20 degrees of freedom
                            # Multiple R-squared:  0.9968,	Adjusted R-squared:  0.9964 
                            # F-statistic:  2099 on 3 and 20 DF,  p-value: < 2.2e-16



# Or pass newdata to predict to estimate the two points of
interest
gdp_1980 <- predict(fit_both3, newdata = data.frame(
  country = c("Albania", "Austria"),
  year = c(1980, 1980))
)
gdp_1980
gdp_1980[2] - gdp_1980[1]

                                      # > gdp_1980
                                      # 1         2 
                                      # 3282.596 20679.202 
                                      # > gdp_1980[2] - gdp_1980[1]
                                      # 2 
                                      # 17396.61 

# Use the Western Collaborative Group Study data to determine if there is a relationship between age and cholesterol level.
# Remember to plot the data first.
# 
# Make a simple regression model. Add other variables to adjust for potential confounding.


# Plot data first
wcgsdata %>%
  ggplot(aes(x = age, y = chol))+
  geom_point() +
  geom_smooth(method = "lm", formula = "y~x")


# Weak positive relationship
# Simple linear regression
dependent <- "chol"
explanatory <- "age"
wcgsdata %>%
  finalfit(dependent, explanatory, metrics = TRUE)

                    # [[1]]
                    # Dependent: Cholesterol (mg/100 ml)                  unit        value    Coefficient (univariable)
                    # Age (years) [39.0,59.0] Mean (sd) 226.4 (43.4) 0.70 (0.43 to 0.98, p<0.001)
                    # Coefficient (multivariable)
                    # 0.70 (0.43 to 0.98, p<0.001)
                    # 
                    # [[2]]
                    # 
                    # Number in dataframe = 3154, Number in model = 3142, Missing = 12, Log-likelihood = -16293.52, AIC = 32593, R-squared = 0.008, Adjusted R-squared = 0.0076


# For each year of age, cholesterol increases by 0.7 mg/100 ml.
# This gradient differs from zero.
# Is this effect independent of other available variables?
# Make BMI as above
dependent <- "chol"
explanatory <- c( "age", "bmi", "sbp", "smoking",
                  "personality_2L")
wcgsdata %>%
  mutate(
    bmi = ((weight*0.4536) / (height*0.0254)^2) %>%
      ff_label("BMI")
  ) %>%
  finalfit(dependent, explanatory, metrics = TRUE)
