
# Read data -------------------------------------------------------------
library(tidyverse)
gbd_full <- read_csv('data/global_burden_disease_cause_year_sex_income.csv')
head(gbd_full)
dim(gbd_full)
names(gbd_full)

# cause                  year sex    income       deaths_millions
#   <chr>                 <dbl> <chr>  <chr>                  <dbl>
# 1 Communicable diseases  1990 Female High                    0.21
# 2 Communicable diseases  1990 Female Upper-Middle            1.15
# 3 Communicable diseases  1990 Female Lower-Middle            4.43
# 4 Communicable diseases  1990 Female Low                     1.51
# 5 Communicable diseases  1990 Male   High                    0.26
# 6 Communicable diseases  1990 Male   Upper-Middle            1.35

#  Creating a single year tibble ------------------------------------------
gbd2017 <- gbd_full %>% filter(year == 2017)
head(gbd2017)

gbd_factored <- gbd_full %>% 
  mutate(factor_cause = factor(cause))

gbd_factored

                      # cause                  year sex    income       deaths_millions factor_cause         
                      #   <chr>                 <dbl> <chr>  <chr>                  <dbl> <fct>                
                      # 1 Communicable diseases  1990 Female High                    0.21 Communicable diseases
                      # 2 Communicable diseases  1990 Female Upper-Middle            1.15 Communicable diseases
                      # 3 Communicable diseases  1990 Female Lower-Middle            4.43 Communicable diseases
                      # 4 Communicable diseases  1990 Female Low                     1.51 Communicable diseases
                      # 5 Communicable diseases  1990 Male   High                    0.26 Communicable diseases
                      # 6 Communicable diseases  1990 Male   Upper-Middle            1.35 Communicable diseases
                      # 7 Communicable diseases  1990 Male   Lower-Middle            4.73 Communicable diseases
                      # 8 Communicable diseases  1990 Male   Low                     1.72 Communicable diseases
                      # 9 Injuries               1990 Female High                    0.2  Injuries             
                      # 10 Injuries               1990 Female Upper-Middle            0.55 Injuries 

gbd_factored$factor_cause %>% levels()
# [1] "Communicable diseases"     "Injuries"                  "Non-communicable diseases"



gbd2017 %>% mutate(income = fct_relevel(income,
                                        'Low',
                                        'Lower-Middle',
                                        'Upper-Middle',
                                        'High')) %>% 
  ggplot(aes(x = sex, y = deaths_millions, fill = income)) + geom_col(position = 'dodge') + 
  facet_wrap(~cause, ncol = 4) + theme(legend.position = 'top')
# x = sex,
# y = deaths_millions,
# fill = cause,
# facet_wrap= ~incomes

### New columns: summarise(), mutate()

#geom --> geometric

# Aggregating: group_by(), summarise() ------------------------------------

# Health data analysis is frequently concerned with making comparisons
# between groups. Groups of genes, or diseases, or patients, or populations,
# etc. An easy approach to the comparison of data by a categorical grouping
# is therefore essential.

gbd2017$deaths_millions %>% sum()
                    # [1] 55.74

gbd2017 %>% summarise(sum(deaths_millions))
                    # `sum(deaths_millions)`
                    # <dbl>
                    #   1                   55.7

gbd2017 %>% 
  group_by(cause) %>%
  summarise(sum(deaths_millions))

                    # cause                     `sum(deaths_millions)`
                    #   <chr>                                      <dbl>
                    # 1 Communicable diseases                      10.4 
                    # 2 Injuries                                    4.47
                    # 3 Non-communicable diseases                  40.9 


gbd2017 %>% 
  group_by(cause, sex) %>% 
  summarise(sum(deaths_millions))
                    # cause                     sex    `sum(deaths_millions)`
                    #   <chr>                     <chr>                   <dbl>
                    # 1 Communicable diseases     Female                   4.91
                    # 2 Communicable diseases     Male                     5.47
                    # 3 Injuries                  Female                   1.42
                    # 4 Injuries                  Male                     3.05
                    # 5 Non-communicable diseases Female                  19.2 
                    # 6 Non-communicable diseases Male                    21.7 


# Add new columns: mutate() -----------------------------------------------
# ungroup()
gbd2017 %>% 
  group_by(cause, sex) %>% 
  summarise(deaths_per_group = sum(deaths_millions)) %>%
  ungroup() %>%
  mutate(deaths_total = sum(deaths_per_group))

                    # cause                     sex    deaths_per_group deaths_total
                    #   <chr>                     <chr>             <dbl>        <dbl>
                    # 1 Communicable diseases     Female             4.91         55.7
                    # 2 Communicable diseases     Male               5.47         55.7
                    # 3 Injuries                  Female             1.42         55.7
                    # 4 Injuries                  Male               3.05         55.7
                    # 5 Non-communicable diseases Female            19.2          55.7
                    # 6 Non-communicable diseases Male              21.7          55.7



# Percentages formatting: percent()
# percent() function for formatting percentages come from library(scales)
library(scales)
gbd2017_summarised <- gbd2017 %>% 
  group_by(cause, sex) %>% 
  summarise(deaths_per_group = sum(deaths_millions)) %>% 
  ungroup() %>%
  mutate(deaths_total = sum(deaths_per_group),
deaths_relative = percent(deaths_per_group / deaths_total))

gbd2017_summarised

                  # cause                     sex    deaths_per_group deaths_total deaths_relative
                  #   <chr>                     <chr>             <dbl>        <dbl> <chr>          
                  # 1 Communicable diseases     Female             4.91         55.7 8.8%           
                  # 2 Communicable diseases     Male               5.47         55.7 9.8%           
                  # 3 Injuries                  Female             1.42         55.7 2.5%           
                  # 4 Injuries                  Male               3.05         55.7 5.5%           
                  # 5 Non-communicable diseases Female            19.2          55.7 34.4%          
                  # 6 Non-communicable diseases Male              21.7          55.7 39.0%   

# round(100*4.91/55.74, 1) %>% paste0("%")

gbd2017_summarised %>%
  mutate(deaths_relative = deaths_per_group / deaths_total)

                # cause                     sex    deaths_per_group deaths_total deaths_relative
                #   <chr>                     <chr>             <dbl>        <dbl>           <dbl>
                # 1 Communicable diseases     Female             4.91         55.7          0.0881
                # 2 Communicable diseases     Male               5.47         55.7          0.0981
                # 3 Injuries                  Female             1.42         55.7          0.0255
                # 4 Injuries                  Male               3.05         55.7          0.0547
                # 5 Non-communicable diseases Female            19.2          55.7          0.344 
                # 6 Non-communicable diseases Male              21.7          55.7          0.390 

# summarise() vs mutate() -------------------------------------------------

# summarise() on grouped data(following group_by()) 
# mutate() on the whole dataset (without using group_by())
gbd_summarised <- gbd2017 %>% 
  group_by(cause, sex) %>%
  summarise(deaths_per_group = sum(deaths_millions)) %>%
  arrange(sex)

gbd_summarised

                # cause                     sex    deaths_per_group
                #   <chr>                     <chr>             <dbl>
                # 1 Communicable diseases     Female             4.91
                # 2 Injuries                  Female             1.42
                # 3 Non-communicable diseases Female            19.2 
                # 4 Communicable diseases     Male               5.47
                # 5 Injuries                  Male               3.05
                # 6 Non-communicable diseases Male              21.7 
##

gbd_summarised_sex <- gbd_summarised %>%
  group_by(sex) %>%
  summarise(deaths_per_sex = sum(deaths_per_group))

gbd_summarised_sex
                # sex    deaths_per_sex
                #   <chr>           <dbl>
                # 1 Female           25.5
                # 2 Male             30.3

##
# But that drops the cause and deaths_per_group columns. One way would
# be to now use a join on gbd_summarised and gbd_summarised_sex:

full_join(gbd_summarised, gbd_summarised_sex)

                # cause                     sex    deaths_per_group deaths_per_sex
                #   <chr>                     <chr>             <dbl>          <dbl>
                # 1 Communicable diseases     Female             4.91           25.5
                # 2 Injuries                  Female             1.42           25.5
                # 3 Non-communicable diseases Female            19.2            25.5
                # 4 Communicable diseases     Male               5.47           30.3
                # 5 Injuries                  Male               3.05           30.3
                # 6 Non-communicable diseases Male              21.7            30.3

# Joining different summaries together can be useful, especially if the
# individual pipelines are quite long (e.g., over 5 lines of %>%). However, it
# does increase the chance of mistakes creeping in and is best avoided if
# possible.


# An alternative is to use mutate() with group_by() to achieve the same
# result as the full_join() above:

gbd_summarised %>%
  group_by(sex) %>%
  mutate(death_per_sex = sum(deaths_per_group))
                # cause                     sex    deaths_per_group death_per_sex
                #  <chr>                     <chr>             <dbl>         <dbl>
                # 1 Communicable diseases     Female             4.91          25.5
                # 2 Injuries                  Female             1.42          25.5
                # 3 Non-communicable diseases Female            19.2           25.5
                # 4 Communicable diseases     Male               5.47          30.3
                # 5 Injuries                  Male               3.05          30.3
                # 6 Non-communicable diseases Male              21.7           30.3

# So mutate() calculates the sums within each grouping variable (in this example just group_by(sex)) 
# and puts the results in a new column without condensing the tibble down or removing any of the existing columns.

gbd2017 %>%
  group_by(cause, sex) %>%
  summarise(deaths_per_group = sum(deaths_millions)) %>%
  group_by(sex) %>%
  mutate(deaths_per_sex = sum(deaths_per_group),
         sex_cause_perc =
           percent(deaths_per_group/deaths_per_sex)) %>%
  arrange(sex, deaths_per_group)

                # cause                     sex    deaths_per_group deaths_per_sex sex_cause_perc
                #   <chr>                     <chr>             <dbl>          <dbl> <chr>         
                # 1 Injuries                  Female             1.42           25.5 6%            
                # 2 Communicable diseases     Female             4.91           25.5 19%           
                # 3 Non-communicable diseases Female            19.2            25.5 75%           
                # 4 Injuries                  Male               3.05           30.3 10.1%         
                # 5 Communicable diseases     Male               5.47           30.3 18.1%         
                # 6 Non-communicable diseases Male              21.7            30.3 71.8% 

# Common arithmetic functions - sum(), mean(), median(), ------------------

# The most common statistics are:
#     - sum()
#     - mean()
#     - median()
#     - min(), max()
#     - sd() - standard deviation
#     - IQR() - interquartile range

mynumbers <- c(1,3, NA)
sum(mynumbers)

sum(mynumbers, na.rm = TRUE)

# select() columns --------------------------------------------------------

# The select() function can be used to choose, rename, or reorder columns of a tibble.
gbd_2rows <- gbd_full %>% 
  slice(1:2)

gbd_2rows

# Let's select() two of these columns:
gbd_2rows %>% 
  select(cause, deaths_millions)

# Use select() to rename the columns we are choosing
gbd_2rows %>% 
  select(cause, deaths = deaths_millions)


# There function rename() is similar to select(), but it keeps all variables whereas select() only kept the ones we mentioned:
gbd_2rows %>% 
  rename(deaths = deaths_millions)

# select() can also be used to reorder the columns in your tibble.
gbd_2rows %>%
  select(year, sex, income, cause, deaths_millions)

# If you want to move specific column(s) to the front of the tibble, do:
gbd_2rows %>% 
  select(year, sex, everything())


# columns that include the word "deaths" that you want to
gbd_2rows %>%
  select(starts_with('deaths'))


# Reshaping data - long vs wide format ------------------------------------
gbd_wide <- read_csv('data/global_burden_disease_wide-format.csv')
gbd_long <- read_csv('data/global_burden_disease_cause-year-sex.csv')

# Pivot values from rows into columns (wider)
gbd_long %>% 
  pivot_wider(names_from = year, values_from = deaths_millions)


gbd_long %>%
  pivot_wider(names_from = sex, values_from = deaths_millions) %>%
  mutate(Male - Female)


dbd_long %>%
  pivot_wider(names_from = c(sex, year), values_from = deaths_millions)


# Pivot values from columns to rows (longer)
gbd_wide %>% 
  pivot_longer(matches("Female|Male"), names_to = "sex_year", values_to = "deaths_millions") %>% slice(1:6)


gbd_wide %>% 
  select(matches("Female|Male"))


# separate() a column into multiple columns
gbd_wide %>%
  # same pivot_longer as before
  pivot_longer(matcheds("Female|Male"), 
               names_to = "sex_year", 
               values_to = "deaths_millions") %>% 
  separate(sex_year, into = c("sex", "year"), sep = '_',convert = TRUE)
# We've also added convert = TRUE to separate() so year would get converted into a numeric variable.

# arrange() rows ----------------------------------------------------------

# The arrange() function sorts rows based on the column(s) you want. By default, it arranges the tibble in ascending order:
gbd_long %>% 
  arrange(deaths_millions) %>% 
  # first 3 rows just for printing 
  slice(1:3)

# For numeric variables, we can just use a - to sort in descending order:
gbd_long %>%
  arrange(-deaths_millions) %>% 
  slice(1:3)


# The - doesn't work for categorical variables; they need to be put in desc() for arranging in descending order:
gbd_long %>%
  arrange(desc(sex)) %>%
  # printing rows 1, 9, 11 and 12
  slice(1, 9, 11, 12)

# Factor levels
# arrange() sorts characters alphabetically, whereas factors will be sorted by
# the order of their levels. Let's make the cause column into a factor:

gbd_factored <- gbd_long %>% 
  mutate(cause = factor(cause))
  

gbd_factored$cause %>% levels()


# But we can now use fct_relevel() inside mutate() to change the order of
# these levels:

gbd_factored <- gbd_factored %>% 
  mutate(cause = cause %>%
           fct_relevel('Injuries'))

gbd_factored$cause %>% levels()


# Exercises ---------------------------------------------------------------
# 1 Exercise - pivot_wider()
# Using the GBD dataset with variables cause, year (1990 and 2017 only), sex

gbd_long <- read_csv('data/global_burden_disease_cause-year-sex.csv')

# Use pivot_wider() to put the cause variable into columns using the deaths_millions as values

# Solution
gbd_long %>% 
  pivot_wider(names_from = cause, values_from = deaths_millions)


# Exercise - group_by(), summarise()
# Read in the full GBD dataset with variables cause, year, sex, income, deaths_millions.

glimpse(gbd_full)

summary_data1 <- gbd_full %>%
  group_by(year) %>%
  summarise(total_per_year = sum(deaths_millions))


summary_data2 <- gbd_full %>% 
  group_by(year, cause) %>%
  summarise(total_per_cause = sum(deaths_millions))
summary_data2

# gbd_full has 168 observations (rows),
# summary_data1 has 7,
# summary_data2 has 21.



# 3 Exercise - full_join(), percent()
# For each cause, calculate its percentage to total deaths in each year.
# Hint: Use full_join() on summary_data1 and summary_data2, and then
# use mutate() to add a new column called percentage.

library(scales)
full_join(summary_data1, summary_data2) %>% 
  mutate(percentage= percent(total_per_cause / total_per_year))



# 4 Exercise - mutate(), summarise()
# Instead of creating the two summarised tibbles and using a full_join(),
# achieve the same result as in the previous exercise with a single pipeline
# using summarise() and then mutate().
# 
# Hint: you have to do it the other way around, so group_by(year, cause)
# %>% summarise(...) first, then group_by(year) %>% mutate().
# 
# Bonus: select() columns year, cause, percentage, then pivot_wider()
# the cause variable using percentage as values.


gbd_full %>% 
  # aggregate to deaths per cause per year using summarise()
  
  group_by(year, cause) %>% 
  summarise(total_per_cause = sum(deaths_millions)) %>%
  
  # then add a column of yearly totals using mutate()
  group_by(year) %>%
  mutate(total_per_year = sum(total_per_cause)) %>%
  
  # add the percentage column
  mutate(percentage = percent(total_per_cause / total_per_year)) %>%
  # select the final variables for better viewing
  select(year, cause, percentage) %>% 
  pivot_wider(names_from = cause, values_from = percentage)




# 5 Exercise - filter(), summarise(), pivot_wider()
#Still working with gbd_full:
#     - Filter for 1990.
#     - Calculate the total number of deaths in the different income groups (High, Upper-Middle, Lower-Middle, Low). 
# Hint: use group_by(income) and summarise(new_column_name = sum(variable)).
#     - Calculate the total number of deaths within each income group for males and females. 
# Hint: this is as easy as adding , sex to group_by(income).
#     - pivot_wider() the income column.

gbd_full %>% 
  filter(year == 1990) %>%
  group_by(income, sex) %>%
  summarise(total_deaths = sum(deaths_millions)) %>%
  pivot_wider(names_from = income, values_from = total_deaths)


