# install.packages('tidyverse')
library(tidyverse)
# ?tidyverse

example_data <- read.csv('data/example_data.csv')
View(example_data)


gbd_short <- read.csv('data/global_burden_disease_cause-year.csv')
View(gbd_short)

################################################################################
#Variable types and why we care
#There are three broad types of data:
#  continuous (numbers), in R: numeric, double, or integer;
#  categorical, in R: character, factor, or logical (TRUE/FALSE);
#  date/time, in R: POSIXct date-time3.
################################################################################