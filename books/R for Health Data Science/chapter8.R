
# Working with categorical outcome ----------------------------------------
## Factors -----------------------------------------------------------------

# Categorical data can be a:
# * Factor
#      – a fixed set of names/strings or numbers
#      – these may have an inherent order (1st, 2nd 3rd) - ordinal factor
#     – or may not (female, male)
# * Character
#      – sequences of letters, numbers, or symbols
# * Logical
#      – containing only TRUE or FALSE

library(tidyverse)
library(finalfit)
theme_set(theme_bw())

meldata <- boot::melanoma

meldata %>% glimpse()
meldata %>% ff_glimpse()


head(meldata)

            # > head(meldata)
            # time status sex age year thickness ulcer
            # 1   10      3   1  76 1972      6.76     1
            # 2   30      3   1  56 1968      0.65     0
            # 3   35      2   1  41 1977      1.34     0
            # 4   99      3   0  71 1968      2.90     0
            # 5  185      1   1  52 1965     12.08     1
            # 6  204      1   1  28 1971      4.84     1

# As can be seen, all of the variables are currently coded as continuous/numeric. 
# The <dbl> stands for ‘double’, meaning numeric which comes from ‘double-precision floating point'.


## Recode the data ---------------------------------------------------------

# In the section below, we convert the continuous variables to factors (e.g., sex %>% factor() %>%), then use the forcats package
# to recode the factor levels. Modern databases (such as REDCap) can give  you an R script to recode your specific dataset. 
# This means you don’t always have to recode your factors from numbers to names manually. But you will always be recoding 
# variables during the  exploration and analysis stages.

meldata <- meldata %>%
  mutate(sex.factor =
           sex %>% 
           factor() %>% 
           fct_recode( 
             "Female" = "0", 
             "Male" = "1") %>%
           ff_label("Sex"), 
       
         ulcer.factor = factor(ulcer) %>%
           fct_recode("Present" = "1",
                      "Absent" = "0") %>%
           ff_label("Ulcerated tumour"),
         
         status.factor = factor(status) %>%
           fct_recode("Died melanoma" = "1",
                      "Alive" = "2",
                      "Died - other causes" = "3") %>%
           ff_label("Status"))

meldata


            #      time status sex age year thickness ulcer sex.factor ulcer.factor       status.factor
            # 1     10      3   1  76 1972      6.76     1       Male      Present Died - other causes
            # 2     30      3   1  56 1968      0.65     0       Male       Absent Died - other causes
            # 3     35      2   1  41 1977      1.34     0       Male       Absent               Alive
            # 4     99      3   0  71 1968      2.90     0     Female       Absent Died - other causes
            # 5    185      1   1  52 1965     12.08     1       Male      Present       Died melanoma
            # 6    204      1   1  28 1971      4.84     1       Male      Present       Died melanoma
            # 7    210      1   1  77 1972      5.16     1       Male      Present       Died melanoma
# ----------------------------------------------------------------------
# summary of age
meldata$age %>% 
  summary()

meldata %>% 
  ggplot(aes(x= age)) +
  geom_histogram()

# There are different ways in which a continuous variable can be converted to a factor. 
# You may wish to create a number of intervals of equal length. The cut() function can be used for this


# Equal intervals vs quantiles --------------------------------------------

meldata <- meldata %>% 
  mutate(age.factor = age %>% 
      cut(4))

meldata$age.factor %>% 
  summary()

          # (3.91,26.8] (26.8,49.5] (49.5,72.2] (72.2,95.1] 
          #      16          68         102          19 

# Quantiles:

meldata <- meldata %>% 
  mutate(age.factor= age %>% 
      Hmisc::cut2(g= 4))

meldata$age.factor %>% 
  summary()

          # [ 4,43) [43,55) [55,66) [66,95] 
          #   55      49      53      48


# Using the cut function, a continuous variable can be converted to a categorical one:

meldata <- meldata %>%
  mutate(
    age.factor =
      age %>%
      cut(breaks = c(4,20,40,60,95), include.lowest = TRUE) %>%
      fct_recode(
        "≤20" = "[4,20]",
        "21 to 40" = "(20,40]",
        "41 to 60" = "(40,60]",
        ">60" = "(60,95]"
      ) %>%
      ff_label("Age (years)")
  )
head(meldata$age.factor)

            # [1] >60      41 to 60 41 to 60 >60      41 to 60 21 to 40
            # Levels: =20 21 to 40 41 to 60 >60
head(meldata)
# 
#    time status sex age year thickness ulcer sex.factor ulcer.factor       status.factor age.factor
# 1   10      3   1  76 1972      6.76     1       Male      Present Died - other causes        >60
# 2   30      3   1  56 1968      0.65     0       Male       Absent Died - other causes   41 to 60
# 3   35      2   1  41 1977      1.34     0       Male       Absent               Alive   41 to 60
# 4   99      3   0  71 1968      2.90     0     Female       Absent Died - other causes        >60
# 5  185      1   1  52 1965     12.08     1       Male      Present       Died melanoma   41 to 60
# 6  204      1   1  28 1971      4.84     1       Male      Present       Died melanoma   21 to 40

### Plot the data -----------------------------------------------------------

# We are interested in the association between tumour ulceration and death from melanoma. 
# To start then, we simply count the number of patients with ulcerated tumours who died. 
# It is useful to plot this as counts but also as proportions. 
# It is proportions you are comparing, but you really want to know the absolute numbers as well.

p1 <- meldata %>%
  ggplot(aes(x= ulcer.factor, fill= status.factor)) +
  geom_bar() +
  theme(legend.position = 'none')

p2 <- meldata %>% 
  ggplot(aes(x= ulcer.factor, fill= status.factor)) +
  geom_bar(position = 'fill') +
  ylab('proportion')

library(patchwork)
p1 + p2

# It should be obvious that more died from melanoma in the ulcerated tumour group compared with the non-ulcerated tumour group. 
# ☺The stacking is orders from top to bottom by default.

p1 <- meldata %>% 
  ggplot(aex(x= ulcer.factor, fill= status.factor)) +
  geom_bar(position = position_stack(reverse = TRUE)) +
  theme(legend.position = 'none')

p2 <- meldata %>% 
  ggplot(aes(x= ulcer.factor, fill= status.factor)) +
  geom_bar(position = position_fill(reverse = TRUE)) +
  ylab('proportion')

library(patchwork)
p1 + p2


# Just from the plot then, death from melanoma in the ulcerated tumour group is around 40% and in the non-ulcerated group around 13%. 
# The number of patients included in the study is not huge, however, this still looks like a real difference given its effect size.
# 
# We may also be interested in exploring potential effect modification, interactions and confounders. 
# Again, we urge you to first visualize these, rather than going straight to a model.

p1 <- meldata %>% 
  ggplot(aes(x= ulcer.factor, fill= status.factor)) +
  geom_bar(position = position_stack(reverse = TRUE)) +
  facet.grid(sex.factor ~ age.factor) +
  theme(legend.position = 'none')

p2 <- meldata %>% 
  ggplot(aes(x= ulcer.factor, fill= status.factor)) +
  geom_bar(position= position_fill(reverse = TRUE)) +
  facet_grid(sex.factor ~ age.factor) +
  theme(legend.position = 'bottom')

#  Facetted bar plot: Outcome after surgery for patients with ulcerated melanoma aggregated by sex and age.

p1 / p2


# Group factor levels together - fct_collapse() ---------------------------

# Our question relates to the association between tumour ulceration and death from melanoma. 
# The outcome measure has three levels as can be seen. For our purposes here, we will generate a disease-specific mortality variable 
# (status_dss), by combining “Died - other causes” and “Alive”.

meldata <- meldata %>% 
  mutate(status_dss= fct_collapse(
    status.factor,
    "Alive" = c("Alive", "Died - other causes"))
  )
 
meldata
# Change the order of values within a factor - fct_relevel() --------------

# The default order for levels with factor() is alphabetical. We often want to reorder the levels in a factor when plotting, 
# or when performing a regression analysis and we want to specify the reference level.
# The order can be checked using levels().


# dss: disease specific survival
meldata$status_dss %>% 
  levels()

              # [1] "Died melanoma" "Alive" 

# The reason “Alive” is second, rather than alphabetical, is it was recoded from “2” and that order was retained. 
# If, however, we want to make comparisons relative to “Alive”, we need to move it to the front by using fct_relevel().

 

          # label  levels Died melanoma     Alive
          # Ulcerated tumour  Absent     16 (28.1) 99 (66.9)
          # Present     41 (71.9) 49 (33.1)


# finalfit is useful for summarising multiple variables. We often want to summarise more than one factor or 
# continuous variable against our dependent variable of interest. Think of Table 1 in a journal article. 
# Any number of continuous or categorical explanatory variables can be added.


library(finalfit)
meldata %>% 
  summary_factorlist(dependent = 'status_dss',
                     explanatory = c('ulcer.factor', 'age.factor', 'sex.factor', 'thickness'))

# Pearson’s chi-squared and Fisher’s exact tests --------------------------

# study from the book


# Base R has reliable functions for all common statistical tests, but they are sometimes a little inconvenient to extract results from. 
# A table of counts can be constructed, either using the to identify columns, or using the with() function.


table(meldata$ulcer.factor, meldata$status_dss)
with(meldata, table(ulcer.factor, status_dss))

# both give same result

    #         Died melanoma Alive
    # Absent            16    99
    # Present           41    49

# When working with older R functions, a useful shortcut is the exposition pipe-operator ( %$%) from the magrittr package, 
# home of the standard forward pipe-operator ( %>%).

library(magrittr)
meldata %$% 
  table(ulcer.factor, status_dss)

# The counts table can be passed to prop.table() for proportions.
meldata %$%
  table(ulcer.factor, status_dss) %>% 
  prop.table(margin= 1)    #  1: row, 2:column

#                           status_dss
# ulcer.factor        Died melanoma     Alive
# Absent                 0.1391304   0.8608696
# Present                0.4555556   0.5444444


# Similarly, the counts table can be passed to chisq.test() to perform the chi-squared test.

meldata %$% 
  table(ulcer.factor, status_dss) %>% 
  chisq.test()

# Pearson's Chi-squared test with Yates' continuity correction
# 
# data:  .
# X-squared = 23.631, df = 1, p-value = 1.167e-06


# The result can be extracted into a tibble using the tidy() function from the broom package.

library(broom)
meldata %$%
  table(ulcer.factor, status_dss) %>% 
  chisq.test() %>% 
  tidy()

# 
      # statistic    p.value parameter method                                                      
          # <dbl>      <dbl>     <int> <chr>                                                       
#   1      23.6 0.00000117         1 Pearson's Chi-squared test with Yates' continuity correction



# The chisq.test() function applies the Yates' continuity correction by default. 
# The standard interpretation assumes that the discrete probability of observed counts in the table can be approximated by the
# continuous chisquared distribution. 
# This introduces some error. 
# The correction involves subtracting 0.5 from the absolute difference between each observed and expected value. 
# This is particularly helpful when counts are low, but can be removed if desired by chisq.test(..., correct = FALSE).


# Fisher’s exact test -----------------------------------------------------

# A commonly stated assumption of the chi-squared test is the requirement to have an expected count of at least 5 in each cell of the 2x2 table. 
# For larger tables, all expected counts should be (>1) and no more than 20% of all cells should have expected counts (<5). 
# If this assumption is not fulfilled, an alternative test is Fisher's exact test. 
# For instance, if we are testing across a 2x4 table created from our age.factor variable and status_dss, then we receive a warning.

meldata %$% 
  table(ulcer.factor, status_dss) %>% 
  fisher.test()

# data:  .
# p-value = 7.134e-07
# alternative hypothesis: true odds ratio is not equal to 1
# 95 percent confidence interval:
#   0.09226445 0.39543158
# sample estimates:
#   odds ratio 
# 0.1948651 

meldata %$% 
  table(ulcer.factor, status_dss) %>% 
  fisher.test() %>% 
  tidy()

      # estimate     p.value conf.low conf.high method                             alternative
        # <dbl>       <dbl>    <dbl>     <dbl> <chr>                              <chr>      
#   1    0.195 0.000000713   0.0923     0.395 Fisher's Exact Test for Count Data two.sided  



# Chi-squared / Fisher’s exact test using finalfit' -----------------------

# It is easier using the summary_factorlist() function from the finalfit package. 
# Including p = TRUE in summary_factorlist() adds a hypothesis test to each included comparison. 
# This defaults to chi-squared tests with a continuity correction for categorical variables.


library(finalfit)
meldata %>% 
  summary_factorlist(dependent = 'status_dss',
                     explanatory = 'ulcer.factor',
                     p = TRUE)

#            label  levels Died melanoma     Alive      p
# Ulcerated tumour  Absent     16 (28.1) 99 (66.9) <0.001
#                  Present     41 (71.9) 49 (33.1) 


# Adding further variables:

library(finalfit)
meldata %>% 
  summary_factorlist(dependent = 'status_dss',
                     explanatory = c('ulcer.factor', 'age.factor', 'sex.factor', 'thickness'),
                     p = TRUE)


# Note that for continuous explanatory variables, an F-test (ANOVA) is performed by default. 
# If variables are considered non-parametric ( cont = "mean"), then a Kruskal-Wallis test is used.
# Switch to Fisher's exact test:

library(finalfit)
meldata %>% 
  summary_factorlist(dependent = 'status_dss',
                     explanatory = c('ulcer.factor', 'age.factor', 'sex.factor', 'thickness'),
                     p = TRUE,
                     p_cat = 'fisher')


# Further options can be included:

meldata %>%
  summary_factorlist(dependent = "status_dss",
                     explanatory = c("ulcer.factor", "age.factor","sex.factor", "thickness"),
                     p = TRUE,
                     p_cat = "fisher",
                     digits = c(1, 1, 4, 2), #1: mean/median, 2:SD/IQR 3: p-value, 4: count percentage
                     na_include = TRUE, # include missing in results/test
                     add_dependent_label = TRUE)