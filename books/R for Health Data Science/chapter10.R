
# Time-to-event data and survival -----------------------------------------

# Get and check the data
library(tidyverse)
library(finalfit)
melanoma <- boot::melanoma

glimpse(melanoma)
missing_glimpse(melanoma)
ff_glimpse(melanoma)


# Recode the data
library(dplyr)
library(forcats)
melanoma <- melanoma %>%
  mutate(
    status_os = if_else(status == 2, 0, 1), 

status_dss = if_else(status == 2, 0, 
if_else(status == 1, 1, 0)), 
status_crr = if_else(status == 2, 0, 
if_else(status == 1, 1, 2)),
age = ff_label(age, "Age (years)"),
thickness = ff_label(thickness, "Tumour thickness (mm)"),
sex = factor(sex) %>%
  fct_recode("Male" = "1",
             "Female" = "0") %>%
  ff_label("Sex"),
ulcer = factor(ulcer) %>%
  fct_recode("No" = "0",
             "Yes" = "1") %>%
  ff_label("Ulcerated tumour")
  )

# Check the above code with Github

# Kaplan Meier survival estimator -----------------------------------------


library(survival)
survival_object <- melanoma %$%
  Surv(time, status_os)

head(survival_object)


# Expressing time in years
survival_object <- melanoma %$% 
  Surv(time/365, status_os)



# KM analysis for whole cohort --------------------------------------------

# Overall survival in whole cohort
my_survfit <- survfit(survival_object ~ 1, data = melanoma)
my_survfit # 205 patients, 71 events


# Life table
summary(my_survfit, times = c(0, 1, 2, 3, 4, 5))



# Kaplan Meier plot -------------------------------------------------------

dependent_os <- "Surv(time/365, status_os)"
explanatory <- c("ulcer")
melanoma %>%
  surv_plot(dependent_os, explanatory, pval = TRUE)



# Cox proportional hazards regression -------------------------------------

library(survival)
coxph(Surv(time, status_os) ~ age + sex + thickness + ulcer,
      data = melanoma) %>%
  summary()



# finalfit() --------------------------------------------------------------

dependent_os <- "Surv(time, status_os)"
dependent_dss <- "Surv(time, status_dss)"
dependent_crr <- "Surv(time, status_crr)"
explanatory <- c("age", "sex", "thickness", "ulcer")
melanoma %>%
  finalfit(dependent_os, explanatory)

# The labelling of the final table can be adjusted as desired.
melanoma %>%
  finalfit(dependent_os, explanatory, add_dependent_label =
             FALSE) %>%
  rename("Overall survival" = label) %>%
  rename(" " = levels) %>%
  rename(" " = all)


# Reduced model -----------------------------------------------------------

explanatory_multi <- c("age", "thickness", "ulcer")
melanoma %>%
  finalfit(dependent_os, explanatory, explanatory_multi, keep_models = TRUE)


# Testing for proportional hazards ----------------------------------------

explanatory <- c("age", "sex", "thickness", "ulcer", "year")
melanoma %>%
  coxphmulti(dependent_os, explanatory) %>%
  cox.zph() %>%
  {zph_result <<- .} %>%
  plot(var=5)


zph_result



# Stratified models -------------------------------------------------------

explanatory <- c("age", "sex", "ulcer", "thickness", "strata(year)")
melanoma %>%
  finalfit(dependent_os, explanatory)


# Correlated groups of observations ---------------------------------------

# Simulate random hospital identifier
melanoma <- melanoma %>%
  mutate(hospital_id = c(rep(1:10, 20), rep(11, 5)))
# Cluster model
explanatory <- c("age", "sex", "thickness", "ulcer", "cluster(hospital_id)")
melanoma %>%
  finalfit(dependent_os, explanatory)



# Frailty model
explanatory <- c("age", "sex", "thickness", "ulcer",  "frailty(hospital_id)")
melanoma %>%
  finalfit(dependent_os, explanatory)



# Hazard ratio plot -------------------------------------------------------

melanoma %>%
  hr_plot(dependent_os, explanatory)


# Competing risks regression ----------------------------------------------

explanatory <- c("age", "sex", "thickness", "ulcer")
dependent_dss <- "Surv(time, status_dss)"
dependent_crr <- "Surv(time, status_crr)"
melanoma %>%
  # Summary table
  summary_factorlist(dependent_dss, explanatory,
                     column = TRUE, fit_id = TRUE) %>%
  # CPH univariable
  ff_merge(
    melanoma %>%
      coxphmulti(dependent_dss, explanatory) %>%
      fit2df(estimate_suffix = " (DSS CPH univariable)") ) %>%
  # CPH multivariable
  ff_merge(
    melanoma %>%
      coxphmulti(dependent_dss, explanatory) %>%
      fit2df(estimate_suffix = " (DSS CPH multivariable)") ) %>%
  # Fine and Gray competing risks regression
  ff_merge(
    melanoma %>%
      crrmulti(dependent_crr, explanatory) %>%
      fit2df(estimate_suffix = " (competing risks multivariable)")  ) %>%
  select(-fit_id, -index) %>%
  dependent_label(melanoma, "Survival")



# Dates in R --------------------------------------------------------------


# Converting dates to survival time ---------------------------------------

library(lubridate)
first_date <- ymd("1966-01-01") # create made-up dates for operations
last_date <- first_date +
  days(nrow(melanoma)-1) # every day from 1- Jan 1966
operation_date <-
  seq(from = first_date,
      to = last_date, by = "1 day") # create dates
melanoma$operation_date <- operation_date # add sequence to melanoma dataset



melanoma <- melanoma %>%
  mutate(censoring_date = operation_date + days(time))
# (Same as doing:):
melanoma$censoring_date <- melanoma$operation_date +
  days(melanoma$time)



melanoma <- melanoma %>%
  mutate(time_days = censoring_date - operation_date)



# This doesn't work
# Surv(melanoma$time_days, melanoma$status==1)
melanoma <- melanoma %>%
  mutate(time_days_numeric = as.numeric(time_days))
# This works as exepcted.
Surv(melanoma$time_days_numeric, melanoma$status.factor == "Died")



# Exercises ---------------------------------------------------------------

# Using the above scripts, perform a univariable Kaplan Meier analysis to determine if ulcer ináuences overall survival. Hint: survival_object ulcer.
# Try modifying the plot produced (see Help for ggsurvplot). For example:
#   - Add in a median survival line: surv.median.line="hv"
# Alter the plot legend: legend.title = "Ulcer Present", legend.labs = c("No", "Yes")
# Change the y-axis to a percentage: ylab = "Probability of survival (%)", surv.scale = "percent"
# Display follow-up up to 10 years, and change the scale to 1 year: xlim = c(0,10), break.time.by = 1)


# ------------------------------------------------------------------------------

# Create a new CPH model, but now include the variable thickness as a variable.
#   How would you interpret the output?
#   Is it an independent predictor of overall survival in this model?
#   Are CPH assumptions maintained?


# Fit model
my_hazard = coxph(survival_object ~ sex + ulcer + age +
                    thickness, data=melanoma)
summary(my_hazard)
# Melanoma thickness has a HR 1.11 (1.03 to 1.18).
# This is interpretted as a 11% increase in the
# risk of death at any time for each 1 mm increase in thickness.
# Check assumptions
ph = cox.zph(my_hazard)
ph
# GLOBAL shows no overall violation of assumptions.
# Plot Schoenfield residuals to evaluate PH
plot(ph, var=4)
