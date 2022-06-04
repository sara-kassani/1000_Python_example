
# Data analysis -----------------------------------------------------------

# Working with continuous outcome variables -----------------------------------------

# Continuous data can be measured.
# Categorical data can be counted.

# The basis for comparisons between continuous measures is the distribution of the data. By distribution, 
# we are simply referring to the shape of the data.


## Get and check the data --------------------------------------------------

# load packages
library(tidyverse)
library(broom)
library(gapminder)
library(finalfit)    #  ff_glimpse, missing_glimpse
# install.packages('finalfit')

gapdata <- gapminder
glimpse(gapdata)

missing_glimpse(gapdata)
ff_glimpse(gapdata)
ff_glimpse(gapdata, levels_cut = 142)    #  142 countries

# As can be seen, there are 6 variables, 4 are continuous and 2 are categorical. 
# The categorical variables are already identified as factors. There are no missing data.



# We will start by comparing life expectancy between the 5 continents of the world in two different years. Always plot your data first. 
# Never skip this step! We are particularly interested in the distribution. There's that word
# again. The shape of the data. Is it normal? Is it skewed? Does it differ between regions and years?
# There are three useful plots which can help here:
#   - Histograms: examine shape of data and compare groups;
#   - Q-Q plots: are data normally distributed?
#   - Box-plots: identify outliers, compare shape and groups.


## Histogram ---------------------------------------------------------------
gapdata %>% 
  filter(year %in% c(2002, 2007)) %>% 
  ggplot(aes(x= lifeExp)) + 
  geom_histogram(bins =  20) +    #  histogram with 20 bars
  facet_grid(year ~ continent)

# What can we see? That life expectancy in Africa is lower than in other regions. 
# That we have little data for Oceania given there are only two countries included, Australia and New Zealand. 
# That Africa and Asia have greater variability in life expectancy by country than in the Americas or Europe. 
# That the data follow a reasonably normal shape, with Africa 2002 a little right skewed.


## Quantile-quantile (Q-Q) plot --------------------------------------------

# It is a graphical method for comparing the distribution (think shape) of our own data to a theoretical distribution, 
# such as the normal distribution. In this context, quantiles are just cut points which divide our data into bins each containing 
# the same number of observations. For example, if we have the life expectancy for 100 countries, then quartiles (note the quar-) 
# for life expectancy are the three ages which split the observations into 4 groups each containing 25 countries. A Q-Q plot 
# simply plots the quantiles for our data against the theoretical quantiles for a particular distribution. If our data follow 
# that distribution (e.g., normal), then our data points fall on the theoretical straight line.

gapdata %>% 
  filter(year %in% c(2002, 2007)) %>%
  ggplot(aes(sample= lifeExp)) +     #  Q-Q plot requires 'sample'
  geom_qq() +     #  defaults to normal distribution
  geom_qq_line(colour = 'blue') + 
  facet_grid(year ~ continent)
  

# We are looking to see if the data (dots) follow the straight line which we included in the plot. These do reasonably, 
# except for Africa which is curved upwards at each end. This is the right skew we could see on the histograms too. 
# If your data  do not follow a normal distribution, then you should avoid using a plotting t-test or ANOVA when comparing groups. 
# Non-parametric tests are one alternative.

# We are frequently asked about the pros and cons of checking for normality using a statistical test, such as the Shapiro-Wilk
# normality test. We don't recommend it. The test is often non-significant when the number of observations is small but the data look
# skewed, and often significant when the number of observations is high but the data look reasonably normal on inspection of plots.
# It is therefore not useful in practice - common sense should prevail.


## Boxplot -----------------------------------------------------------------

# Boxplots are our preferred method for comparing a continuous variable such as life expectancy across a categorical explanatory variable. 
# For continuous data, box plots are a lot more appropriate than bar plots with error bars (also known as dynamite plots).

# 
# The box represents the median (bold horizontal line in the middle) and interquartile range (where 50% of the data sits).
# The lines (whiskers) extend to the lowest and highest values that are still within 1.5 times the interquartile range. 
# Outliers (anything outwith the whiskers) are represented as points.
# 
# The boxplot thus contains information not only on central tendency (median), but on the variation in the data and 
# the distribution of the data, for instance a skew should be obvious.


gapdata %>% 
  filter(year %in% c(2002, 2007)) %>%
  ggplot(aes(x= continent, y= lifeExp)) +
  geom_boxplot() +
  facet_wrap(~ year)

# The median life expectancy is lower in Africa than in any other continent. 
# The variation in life expectancy is greatest in Africa and smallest in Oceania. The data in Africa looks skewed, 
# particularly in 2002 - the lines/whiskers are unequal lengths. can add further arguments to adjust the plot to our liking.
# 
# We particularly encourage the inclusion of the actual data points, here using geom_jitter().

gapdata %>% 
  filter(year %in% c(2002, 2007)) %>%
  ggplot(aes(x= factor(year), y= lifeExp)) +
  geom_boxplot(aes(fill= continent)) +    #  add color to boxplot
  geom_jitter(alpha= 0.4) +
  facet_wrap(~ continent, ncol= 5) +    #  spread by continent
  theme(legend.position = "none") +    #  remove legend
  xlab('Year') +    #  label x-axis
  ylab('Life expectancy (years)') +    #  label y-axis
  ggtitle('Life epectancy by continent in 2002 vs 2007')    #  add title


## Compare the means of two groups -----------------------------------------

# t-test ---
# t-test is used to compare the means of two groups of continuous measurements.

# There are a few variations of the t-test. We will use two here. 
# The most useful in our context is a two-sample test of independent groups. 
# Repeated measures data, such as comparing the same countries in different years, can be analysed using a paired t-test.


# Two-sample t-tests ------------------------------------------------------

# let's compare life expectancy between Asia and Europe for 2007.

# By running the two-sample t-test here, we make the assumption that life expectancy in each country represents 
# an independent measurement of life expectancy in the continent as a whole. This isn't quite right if you think about it carefully.


# So in our example of countries and continents, you have to assume that the mean life expectancy of each country does not 
# depend on the life expectancies of other countries in the group. In other words, that each measurement is independent.

ttest_data <- gapdata %>%
  filter(year == 2007) %>%
    filter(continent %in% c('Asia', 'Europe'))

ttest_result <- ttest_data %>%
  t.test(lifeExp ~ continent, data= .)
  
ttest_result


# The Welch two-sample t-test is the most ?exible and copes with differences in variance (variability) between groups, 
# as in this example. The difference in means is provided at the bottom of the output. The t-value, degrees of freedom (df) 
# and p-value are all provided. The p-value is 0.00003.

# The p-value, for instance, can be accessed
ttest_result$p.value

# The confidence interval of the difference in mean life expectancy between the two continents
ttest_result$conf.int


# Paired t-tests ----------------------------------------------------------

# Consider that we want to compare the difference in life expectancy in Asian countries between 2002 and 2007. 
# The overall difference is not impressive in the boxplot.
# 
# We can plot differences at the country level directly. Change in life expectancy in Asian countries from 2002 to 2007.

paired_data <- gapdata %>%
  filter(year %in% c(2002, 2007)) %>%
  filter(continent == 'Asia') 

paired_data %>%
  ggplot(aes(x= year, y= lifeExp, group= country)) +
  geom_line()


# What is the difference in life expectancy for each individual country? We don't usually have to produce this directly, 
# but here is one method.

paired_table <- paired_data %>%        # save object paired_data
  select(country, year, lifeExp) %>%   # select vars interest
  pivot_wider(names_from = year,       # put years in columns
              values_from = lifeExp) %>% 
  mutate(dlifeExp = `2007` - `2002`)         # difference in means


paired_table


# Mean of difference in years
paired_table %>% summarise(mean(dlifeExp))
# 1.49

# On average, therefore, there is an increase in life expectancy of 1.5 years in Asian countries between 2002 and 2007. 
# Let's test whether this number differs from zero with a paired t-test:

paired_data %>%
  t.test(lifeExp ~ year,data = ., paired= TRUE)


          # data:  lifeExp by year
          # t = -14.338, df = 32, p-value = 1.758e-15
          # alternative hypothesis: true difference in means is not equal to 0
          # 95 percent confidence interval:
          #   -1.706941 -1.282271
          # sample estimates:
          #   mean of the differences 
          # -1.494606 


# The results show a highly significant difference (p-value = 0.000000000000002). 
# The average difference of 1.5 years is highly consistent between countries, as shown on the line plot, and this differs from zero.
# It is up to you the investigator to interpret the relevance of the effect size of 1.5 years in reporting the finding. 
# A highly significant p-value does not necessarily mean there is a (clinically) significant change between the two groups 
# (or in this example, two time points).
# # 


# What if I run the wrong test? -------------------------------------------

# As an exercise, we can repeat this analysis comparing these data in an unpaired manner. The resulting (unpaired) p-value is 0.460.
# Remember, a paired t-test of the same data (life expectancies of Asian countries in 2002 and 2007) showed a very different,
# significant result. In this case, running an unpaired two-sample t-test is just wrong - as the data are indeed paired.

# 
# It is important that the investigator really understands the data and the underlying processes/relationships within it.

# Compare the mean of one group: one sample t-tests -----------------------

# We can use a t-test to determine whether the mean of a distribution is different to a specific value. 
# For instance, we can test whether the mean life expectancy in each continent was significantly different from 77 years in 2007.

gapdata %>% 
  filter(year == 2007) %>%
  group_by(continent) %>%
  do(t.test(.$lifeExp, mu= 77) %>% 
       tidy()
       )

# The mean life expectancy for Europe and Oceania do not significantly differ from 77, while the others do. 
# In particular, look at the confidence intervals of the results above ( conf.low and conf.high columns) and whether they include or exclude 77. 
# For instance, Oceania's confidence intervals are especially wide as the dataset only includes two countries. 
# Therefore, we can't conclude that its value isn't different to 77, but that we don't have enough observations and
# the estimate is uncertain. It doesn't make sense to report the results of a statistical test - whether the p-value is 
# significant or not - without assessing the confidence intervals.


# Interchangeability of t-tests -------------------------------------------

# We can use these differences for each pair of observations (country's life expectancy in 2002 and 2007) to run a simple 
# one-sample t-test instead:

# note that we're using dlifeExp so the differences we calculated above

t.test(paired_table$dlifeExp, mu= 0)

          # One Sample t-test
          # 
          # data:  paired_table$dlifeExp
          # t = 14.338, df = 32, p-value = 1.758e-15
          # alternative hypothesis: true mean is not equal to 0
          # 95 percent confidence interval:
          #   1.282271 1.706941
          # sample estimates:
          #   mean of x 
          # 1.494606

# Notice how this result is identical to the paired t-test.


# Compare the means of more than two groups -------------------------------

# It may be that our question is set around a hypothesis involving more than two groups. 
# For example, we may be interested in comparing life expectancy across 3 continents such as the Americas, Europe and Asia.


# plot the data

gapdata %>%
  filter(year == 2007) %>%
  filter(continent %in% c('Asia', 'Europe', 'Americas')) %>%
  ggplot(aes(x= continent, y= lifeExp)) +
  geom_boxplot()


# ANOVA -------------------------------------------------------------------

# Analysis of variance is a collection of statistical tests which can be used to test the difference in means between two or 
# more groups. In base R form, it produces an ANOVA table which includes an F-test. 
# This so-called omnibus test tells you whether there are any differences in the comparison of means of the included groups. 
# 
# Again, it is important to plot carefully and be clear what question you are asking.

aov_data <- gapdata %>%
  filter(year == 2007) %>%
  filter(continent %in%  c('Asia', 'Europe', 'Americas'))

fit = aov(lifeExp ~ continent, data = aov_data)
summary(fit)

            # Df Sum Sq Mean Sq F value   Pr(>F)    
            # continent    2  755.6   377.8   11.63 3.42e-05 ***
            #   Residuals   85 2760.3    32.5                     
            # ---
            #   Signif. codes:  0 '***' 0.001 '**' 0.01 '*' 0.05 '.' 0.1 ' ' 1


# We can conclude from the signi?cant F-test that the mean life expectancy across the three continents is not the same. 
# This does not mean that all included groups are signi?cantly different from each other. 
# 
# As above, the output can be neatened up using the tidy function.

gapdata %>%
  filter(year == 2007) %>%
  filter(continent %in%  c('Asia', 'Europe', 'Americas')) %>%
  aov(lifeExp ~ continent, data = .) %>%
  tidy()

                  # term         df sumsq meansq statistic    p.value
                  # <chr>     <dbl> <dbl>  <dbl>     <dbl>      <dbl>
                  # 1 continent     2  756.  378.       11.6  0.0000342
                  # 2 Residuals    85 2760.   32.5      NA   NA     

# library(ggfortify) includes a function called autoplot() that can be used to quickly create diagnostic plots,
# including the Q-Q plot that we showed before:

install.packages('ggfortify')
library(ggfortify)
autoplot(fit)

# Multiple testing --------------------------------------------------------

## Pairwise testing and multiple comparisons -------------------------------

# When the F-test is signi?cant, we will often want to determine where the differences lie. 
# This should of course be obvious from the boxplot you have made. However, some are ?xated on the p-value!

pairwise.t.test(aov_data$lifeExp, aov_data$continent, p.adjust.method = 'bonferroni')

                # Pairwise comparisons using t tests with pooled SD 
                # 
                # data:  aov_data$lifeExp and aov_data$continent 
                # 
                # Americas Asia   
                # Asia   0.180    -      
                #   Europe 0.031    1.9e-05
                # 
                # P value adjustment method: bonferroni 


# We have to keep in mind that the p-value's significance level of 0.05 means we have a 5% chance of ?
# Finding a difference in our samples which doesn't exist in the overall population.
# Therefore, the more statistical tests performed, the greater the chances of a false positive result.
# This is also known as type I error - finding a difference when no difference exists.


# The ``Bonferroni'' correction is the most famous and most conservative, where the threshold for significance is lowered in
# proportion to the number of comparisons made. For example, if three comparisons are made, the threshold for significance 
# should be lowered to 0.017.
# 
# Equivalently, all p-values should be multiplied by the number of tests performed.
# 
# The adjusted values can then be compared to a threshold of 0.05, as is the case above. 
# The Bonferroni method is particularly conservative, meaning that type II errors may occur (failure to identify true differences, 
#  or false negatives) in favour or minimizing type I errors (false positives).
 
# The third approach controls for something called false-discovery rate. The development of these methods has been driven in part by
# the needs of areas of science where many different statistical tests are performed at the same time, for instance, examining the
# influence of 1000 genes simultaneously. In these hypothesis-generating settings, a higher tolerance to type I errors may be preferable
# to missing potential findings through type II errors. You can see in our example, that the p-values are lower with the fdr correction
# than the Bonferroni correction ones.


pairwise.t.test(aov_data$lifeExp, aov_data$continent, p.adjust.method = 'fdr')

                      # Pairwise comparisons using t tests with pooled SD 
                      # 
                      # data:  aov_data$lifeExp and aov_data$continent 
                      # 
                      # Americas Asia   
                      # Asia   0.060    -      
                      #   Europe 0.016    1.9e-05
                      # 
                      # P value adjustment method: fdr 


# 
# what is the actual difference in life expectancy in years, rather than the p-value of a comparison test. Choose a method which fits
# with your overall aims. If you are generating hypotheses which you will proceed to test with other methods, the fdr approach may be
# preferable. If you are trying to capture robust effects and want to minimize type II errors, use a family-wise approach.  
# If your head is spinning at this point, don't worry. The rest of the book will continuously revisit these and other similar concepts
# e.g., ``know your data'', ``be sensible, look at the effect size'', using several different examples and datasets. 
# So do not feel like you should be able to understand everything immediately. Furthermore, these things are easier to 
# conceptualize when using your own dataset - especially if that's something you've put your blood, sweat and tears into collecting.


# Non-parametric tests ----------------------------------------------------

# What if your data is a different shape to normal, or the ANOVA assumptions are not fulfilled?

# For instance, if you are examining length of hospital stay it is likely that your data are highly right skewed - most patients are
# discharged from hospital in a few days while a smaller number stay for a long time. 
# Is a comparison of means ever going to be the correct approach here? Perhaps you should consider a time-to-event analysis for instance.
# 
# If a comparison of means approach is reasonable, but the normality assumption is not fulfilled there are two approaches,
# 
# 1. Transform the data;
# 2. Perform non-parametric tests.


### Transforming data -------------------------------------------------------

# Remember, the Welch t-test is reasonably robust to divergence from the normality assumption, so small deviations can be safely
# ignored. Otherwise, the data can be transformed to another scale to deal with a skew. A natural log scale is common.


# Note:
#   If data contain zero values, add a small constant to all values.


africa2002 <- gapdata %>% 
  filter(year == 2002) %>%
  filter(continent == 'Africa') %>% 
  select(country, lifeExp) %>%
  mutate(lifeExp_log = log(lifeExp))

head(africa2002)

              # country      lifeExp lifeExp_log
              # <fct>          <dbl>       <dbl>
              #   1 Algeria         71.0        4.26
              # 2 Angola          41.0        3.71
              # 3 Benin           54.4        4.00
              # 4 Botswana        46.6        3.84
              # 5 Burkina Faso    50.6        3.92
              # 6 Burundi         47.4        3.86

africa2002 %>%
  pivot_longer(contains('lifeExp')) %>%
  ggplot(aes(x= value)) + 
  geom_histogram(bins = 15) + 
  facet_wrap(~name, scales = 'free')



# Non-parametric test for comparing two groups ----------------------------
# 
# The Mann-Whitney U test is also called the Wilcoxon rank-sum test and uses a rank-based method to compare two groups (note the
# Wilcoxon signed-rank test is for paired data). Rank-based just means ordering your
# grouped continuous data from smallest to largest value and assigning a rank (1, 2, 3 .) to each measurement.


# We can use it to test for a difference in life expectancies for African countries between 1982 and 2007. Let's do a histogram,
# Q-Q plot and boxplot first.

africa_data <- gapdata %>% 
  filter(year %in% c(1982, 2007)) %>% 
  filter(continent %in% 'Africa')


p1 <- africa_data %>%
  ggplot(aes(x= lifeExp)) + 
  geom_histogram(bins = 15) + 
  facet_wrap(~year)

p2 <- africa_data %>%
  ggplot(aes(sample = lifeExp)) +    #  sample for q-q plot
  geom_qq() +
  geom_qq_line(color = 'deepskyblue') +
  facet_wrap(~year)

p3 <- africa_data %>%
  ggplot(aes(x= factor(year), y= lifeExp)) + 
  geom_boxplot(aes(fill = factor(year))) +
  geom_jitter(alpha = 0.4) +
  theme(legend.position = 'none')


library(patchwork)
p1 / p2 | p3

# The data is a little skewed based on the histograms and Q-Q plots. The difference between 1982 and 2007 is not particularly striking
# on the boxplot.

africa_data %>%
  wilcox.test(lifeExp ~ year, data= .)

              # Wilcoxon rank sum test with continuity correction
              # 
              # data:  lifeExp by year
              # W = 1130, p-value = 0.1499
              # alternative hypothesis: true location shift is not equal to 0


## Non-parametric test for comparing more than two groups ------------------
# The non-parametric equivalent to ANOVA, is the Kruskal-Wallis test. It can be used in base R, or via the finalfit package.

gapdata %>% 
  filter(year == 2007) %>%
  filter(continent %in% c('Asia', 'Europe', 'Americas')) %>% 
  kruskal.test(lifeExp~continent, data= .) %>% 
  tidy()

              # statistic   p.value parameter method                      
              # <dbl>     <dbl>     <int> <chr>                       
              #   1      21.6 0.0000202         2 Kruskal-Wallis rank sum test


# Finalfit approach -------------------------------------------------------

# The Finalfit package provides an easy to use interface for performing nonparametric hypothesis tests. Any number of explanatory
# variables can be tested against a so-called dependent variable.

dependent <- 'year'
explanatory <- c('lifeExp', 'pop', 'gdpPercap')

africa_data %>% 
  mutate(
    year = factor(year)
  ) %>% 
  summary_factorlist(dependent, explanatory, cont= 'median', p= TRUE)

    # label       levels                               1982                                 2007     p
    # lifeExp Median (IQR)                50.8 (45.6 to 56.6)                  52.9 (47.8 to 59.4) 0.149
    # pop Median (IQR) 5668228.5 (1569553.8 to 9788207.8) 10093310.5 (2909226.5 to 19363654.5) 0.033
    # gdpPercap Median (IQR)           1323.7 (828.7 to 2787.6)             1452.3 (863.0 to 3993.5) 0.503

# Note that the p-values above have not been corrected for multiple testing.

# If you wish to consider only some variables as non-parametric and summarise with a median, then this can be specified using:

dependent <- 'year'
explanatory <- c('lifeExp', 'pop', 'gdpPercap')

africa_data %>% 
  mutate(
    year = factor(year)
  ) %>% 
  summary_factorlist(dependent, explanatory, cont_nonpara= c(1, 3),     #  # variable 1&3 are non-parametric
                     cont_range = TRUE,     #  lower and upper quartile
                     p= TRUE,
                     p_cont_para = 't.test',    #  use t.test/aov for parametric
                     add_row_totals = TRUE,
                     include_row_missing_col = FALSE,
                     add_dependent_label = TRUE
                     ) 


# Dependent: year     Total N                                  1982                     2007     p
# lifeExp 104 (100.0) Median (IQR)      50.8 (45.6 to 56.6)      52.9 (47.8 to 59.4) 0.149
# pop 104 (100.0)    Mean (SD)   9602857.4 (13456243.4)  17875763.3 (24917726.2) 0.038
# gdpPercap 104 (100.0) Median (IQR) 1323.7 (828.7 to 2787.6) 1452.3 (863.0 to 3993.5) 0.503


# Exercises ---------------------------------------------------------------

# Make a histogram, Q-Q plot, and a box-plot for the life expectancy for a continent of your choice, but for all years. 
# Do the data appear normally distributed?

# Solution: 
# make a histogram, q-q plot, and a boxplot for the life expectancy:
# Do the data appear normally distributed?
asia_data <- gapdata %>% 
  filter(continent %in% c('Asia'))

p1 <- asia_data %>% 
  ggplot(aes(x= lifeExp)) +
  geom_histogram(bins = 15)

p2 <- asia_data %>% 
  ggplot(aes(sample= lifeExp)) +
  geom_qq() +
  geom_qq_line(color= 'deepskyblue')

p3 <- asia_data %>% 
  ggplot(aes(x= year, y= lifeExp)) +
  geom_boxplot(aes(fill = factor(year))) +
  geom_jitter(alpha= 0.4) +
  theme(legend.position = 'none')

library(patchwork)
p1 / p2 | p3

# 1. Select any 2 years in any continent and perform a t-test to determine whether mean life expectancy is significantly different.
# Remember to plot your data first.

# 2. Extract only the p-value from your t.test() output.

asia_2years <- asia_data %>% 
  filter(year %in% c(1952, 1972)) 

p1<- asia_2years %>% 
  ggplot(aes(x= lifeExp)) +
  geom_histogram(bins= 15) +
  facet_wrap(~year)



p2 <- asia_2years %>%  
  ggplot(aes(sample= lifeExp)) +
  geom_qq() +
  geom_qq_line(color= 'deepskyblue') +
  facet_wrap(~year)

p3 <- asia_2years %>% 
  ggplot(aes(x= factor(year),  lifeExp)) +
  geom_boxplot(aes(fill= factor(year))) +
  geom_jitter(alpha= 0.4) +
  theme(legend.position = 'none')


library(patchwork)
p1 / p2 | p3



asia_2years %>% 
  t.test(lifeExp ~ year, data= .)


              # Welch Two Sample t-test
              # 
              # data:  lifeExp by year
              # t = -4.7007, df = 63.869, p-value = 1.428e-05
              # alternative hypothesis: true difference in means between group 1952 and group 1972 is not equal to 0
              # 95 percent confidence interval:
              #   -15.681981  -6.327769
              # sample estimates:
              #   mean in group 1952 mean in group 1972 
              # 46.31439           57.31927 

# In 2007, in which continents did mean life expectancy differ from 70

gapdata %>% 
  filter(year == 2007) %>% 
  group_by(continent) %>% 
  do(
  t.test(.$lifeExp, mu= 70) %>% 
    tidy()
)

          # # Groups:   continent [5]
          # continent estimate statistic  p.value parameter conf.low conf.high method            alternative
          # <fct>        <dbl>     <dbl>    <dbl>     <dbl>    <dbl>     <dbl> <chr>             <chr>      
          #   1 Africa        54.8   -11.4   1.33e-15        51     52.1      57.5 One Sample t-test two.sided  
          # 2 Americas      73.6     4.06  4.50e- 4        24     71.8      75.4 One Sample t-test two.sided  
          # 3 Asia          70.7     0.525 6.03e- 1        32     67.9      73.6 One Sample t-test two.sided  
          # 4 Europe        77.6    14.1   1.76e-14        29     76.5      78.8 One Sample t-test two.sided  
          # 5 Oceania       80.7    20.8   3.06e- 2         1     74.2      87.3 One Sample t-test two.sided  

# 1. Use ANOVA to determine if the population changed significantly through the 1990s/2000s in individual continents.

gapdata %>% 
  filter(year >= 1990) %>% 
  ggplot(aes(x= factor(year), y= pop)) +
  geom_boxplot() +
  facet_wrap(~continent)

gapdata %>% 
  filter(year >= 1990) %>% 
  group_by(continent) %>%
  do(
    kruskal.test(pop ~ year, data= .) %>% 
      tidy()
  )
          # 
          # # Groups:   continent [5]
          # continent statistic p.value parameter method                      
          # <fct>         <dbl>   <dbl>     <int> <chr>                       
          #   1 Africa        2.10    0.553         3 Kruskal-Wallis rank sum test
          # 2 Americas      0.847   0.838         3 Kruskal-Wallis rank sum test
          # 3 Asia          1.57    0.665         3 Kruskal-Wallis rank sum test
          # 4 Europe        0.207   0.977         3 Kruskal-Wallis rank sum test
          # 5 Oceania       1.67    0.644         3 Kruskal-Wallis rank sum test
