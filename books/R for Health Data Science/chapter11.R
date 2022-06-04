
# The problem of missing data ---------------------------------------------

# Create some extra missing data
library(finalfit)
library(dplyr)
set.seed(1)
colon_s <- colon_s %>%
  mutate(
    ## Smoking missing completely at random
    smoking_mcar = sample(c("Smoker", "Non-smoker", NA),
                          n(), replace=TRUE,
                          prob = c(0.2, 0.7, 0.1)) %>%
      factor() %>%
      ff_label("Smoking (MCAR)"),
    ## Smoking missing conditional on patient sex
    smoking_mar = ifelse(sex.factor == "Female",
                         sample(c("Smoker", "Non-smoker", NA),
                                sum(sex.factor == "Female"),
                                replace = TRUE,
                                prob = c(0.1, 0.5, 0.4)),
                         
                         sample(c("Smoker", "Non-smoker", NA),
                                sum(sex.factor == "Male"),
                                replace=TRUE, prob = c(0.15,
                                                       0.75, 0.1))
    ) %>%
      factor() %>%
      ff_label("Smoking (MAR)")
  )

# We will then examine our variables of interest using ff_glimpse():
explanatory <- c("age", "sex.factor", "nodes", "obstruct.factor","smoking_mcar", "smoking_mar")
dependent <- "mort_5yr"
colon_s %>%
  ff_glimpse(dependent, explanatory)


# You don’t need to specify the variables, and if you don’t, ff_glimpse() will summarise all variables:

colon_s %>%
  ff_glimpse()


# Identify missing values in each variable: missing_plot() ----------------

colon_s %>%
  missing_plot(dependent, explanatory)


# Look for patterns of missingness: missing_pattern() ---------------------

explanatory <- c("age", "sex.factor", "obstruct.factor", "smoking_mcar", "smoking_mar")

dependent <- "mort_5yr"
colon_s %>%
  missing_pattern(dependent, explanatory)


# Including missing data in demographics tables ---------------------------

# Explanatory or confounding variables
explanatory <- c("age", "sex.factor", "nodes", "smoking_mcar", "smoking_mar")
# Explanatory variable of interest
dependent <- "obstruct.factor" # Bowel obstruction
table1 <- colon_s %>%
  summary_factorlist(dependent, explanatory,
                     na_include=TRUE, na_include_dependent =TRUE,
                     total_col = TRUE, add_col_totals = TRUE,
                     p=TRUE)

table1

# Check for associations between missing and observed data
explanatory <- c("age", "sex.factor", "nodes", "obstruct.factor", "smoking_mcar", "smoking_mar")
dependent <- "mort_5yr"
colon_s %>%
  missing_pairs(dependent, explanatory)



colon_s %>%
  missing_pairs(dependent, explanatory, position = "fill")



# We can also confirm this by using missing_compare():
explanatory <- c("age", "sex.factor", "nodes", "obstruct.factor")
dependent <- "smoking_mcar"

missing_mcar <- colon_s %>%
  missing_compare(dependent, explanatory)
missing_mcar



dependent <- "smoking_mar"
missing_mar <- colon_s %>%
  missing_compare(dependent, explanatory)
missing_mar



# For those who like an omnibus test --------------------------------------
install.packages('MissMech')

library(MissMech)
explanatory <- c("age", "nodes")
dependent <- "mort_5yr"
colon_s %>%
  select(all_of(explanatory)) %>%
  MissMech::TestMCARNormality()



# Handling missing data: MCAR ---------------------------------------------


### Common solution: row-wise deletion --------------------------------------

explanatory <- c("age", "sex.factor", "nodes", "obstruct.factor", "smoking_mcar")
dependent <- "mort_5yr"
fit = colon_s %>%
  finalfit(dependent, explanatory)

fit



# Handling missing data: MAR ----------------------------------------------

### Common solution: Multivariate Imputation by Chained ---------------------
# Multivariate Imputation by Chained Equations (mice)
library(finalfit)
library(dplyr)
library(mice)
explanatory <- c("age", "sex.factor", "nodes", "obstruct.factor", "smoking_mar")
dependent <- "mort_5yr"


# Choose which variable to input missing values for and which variables to use for the imputation process.
colon_s %>%
  select(dependent, explanatory) %>%
  missing_predictorMatrix(
    drop_from_imputed = c("obstruct.factor", "mort_5yr")
  ) -> predM


# Make 10 imputed datasets and run our logistic regression analysis on each set.


fits <- colon_s %>%
  select(dependent, explanatory) %>%
  # Usually run imputation with 10 imputed sets, 4 here for demonstration
mice(m = 4, predictorMatrix = predM) %>%
  # Run logistic regression on each imputed set
  with(glm(formula(ff_formula(dependent, explanatory)),
           family="binomial"))



# Extract metrics from each model

# Examples of extracting metrics from fits and taking the mean
## AICs
fits %>%
  getfit() %>%
  purrr::map(AIC) %>%
  unlist() %>%
  mean()

# C-statistic
fits %>%
  getfit() %>%
  purrr::map(~ pROC::roc(.x$y, .x$fitted)$auc) %>%
  unlist() %>%
  mean()


# Pool models together ----------------------------------------------------

# Pool results
fits_pool <- fits %>%
  pool()
## Can be passed to or_plot
colon_s %>%
  or_plot(dependent, explanatory, glmfit = fits_pool, table_text_size=4)

# Summarise and put in table
fit_imputed <- fits_pool %>%
  fit2df(estimate_name = "OR (multiple imputation)", exp =
           TRUE)
# Use finalfit merge methods to create and compare results
explanatory <- c("age", "sex.factor", "nodes", "obstruct.factor", "smoking_mar")
table_uni_multi <- colon_s %>%
  finalfit(dependent, explanatory, keep_fit_id = TRUE)
explanatory = c("age", "sex.factor", "nodes", "obstruct.factor")
fit_multi_no_smoking <- colon_s %>%
  glmmulti(dependent, explanatory) %>%
  fit2df(estimate_suffix = " (multivariable without smoking)")
# Combine to final table
table_imputed <-
  table_uni_multi %>%
  ff_merge(fit_multi_no_smoking) %>%
  ff_merge(fit_imputed, last_merge = TRUE)



# There is an alternative method to model the missing data for the categorical in this setting – just consider the missing data as 
# a factor level. This has the advantage of simplicity, with the disadvantage of increasing the number of terms in the model.

library(dplyr)
explanatory = c("age", "sex.factor","nodes", "obstruct.factor", "smoking_mar")
fit_explicit_na = colon_s %>%
  mutate(
    smoking_mar = forcats::fct_explicit_na(smoking_mar)
  ) %>%
  finalfit(dependent, explanatory)


