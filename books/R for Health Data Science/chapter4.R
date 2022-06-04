
# Library and Data --------------------------------------------------------

library(tidyverse)
# install.packages('gapminder')
library(gapminder)
glimpse(gapminder)


gapminder$year %>% unique()
gapminder$country %>% n_distinct()    #  142 --> # of countries
gapminder$continent %>% unique()    #  Levels: Africa Americas Asia Europe Oceania

# Note: The name of the package is ggplot2, but the function is called ggplot().

# create a new shorter tibble called gapdata2007 that only includes data for the year 2007.
gapdata2007 <- gapminder %>% 
  filter(year == 2007)

gapdata2007


# loads the gapminder dataset from the package environment into your global environment
gapdata <- gapminder
gapdata

# Anatomy of ggplot explained ---------------------------------------------
gapdata2007 %>% ggplot(aes(x = gdpPercap, y = lifeExp))

# the above code is equivalent to:
# ggplot(gapdata2007, aes(x = gdpPercap, y = lifeExp))

# Draw points for each observation by adding geom_point():
gapdata2007 %>% ggplot(aes(x= gdpPercap, y= lifeExp)) + geom_point()   #  x: continuous variable --> scatter plot
gapdata2007 %>% ggplot(aes(x= continent, y= lifeExp)) + geom_point()   #  x: categorical variable --> strip plot


# let's use continent to give the points some color
gapdata2007 %>% ggplot(aes(x= gdpPercap, y= lifeExp, colour= continent)) + geom_point()

# ?geom_point  # 0, 1, 2, 4, 8, 15, 16, 17, 21, 22, 23

gapdata2007 %>% ggplot(aes(x= gdpPercap, y= lifeExp, color= continent)) + geom_point(shape= 8)


# Faceting is a way to efficiently create the same plot for subgroups within the dataset.
gapdata2007 %>% ggplot(aes(x= gdpPercap, y= lifeExp, color= continent)) + geom_point(shape= 8) + facet_wrap(~continent)

# Note that we have to use the tilde ( ) in facet_wrap(). There is a similar function called facet_grid() that 
# will create a grid of plots based on two grouping variables, e.g., facet_grid(var1 var2). Furthermore, facets are 
# happy to quickly separate data based on a condition

gapdata2007 %>% ggplot(aes(x= gdpPercap, y= lifeExp, color= continent)) + geom_point(shape= 8) + facet_wrap(~pop>50000000)    #  filtering condition (e.g., population 50 million) directly inside a facet_wrap().
# On this plot, the facet FALSE includes countries with a population less than 50 million people, and the facet TRUE includes 
# countries with a population greater than 50 million people.


# Note: The tilde (~) in R denotes dependency. It is mostly used by statistical models to define dependent and explanatory variables.

# theme_bw() ("background white") to give the plot a different look.
gapdata2007 %>% ggplot(aes(x= gdpPercap, y= lifeExp, color= continent)) +
  geom_point(shape= 8) + 
  facet_wrap(~continent)+
  theme_bw()


# Set your theme - grey vs white ------------------------------------------

# set the theme at the beginning of the file (tight after including libraries) to be applied to every plot you draw
library(tidyverse)
theme_set(theme_bw())



# Scatter plots/bubble plots ----------------------------------------------

# bubble plot: size= pop

gapdata2007 %>% ggplot(aes(x= gdpPercap/1000, y= lifeExp, size= pop, color= continent)) + geom_point()

gapdata2007 %>% ggplot(aes(x= gdpPercap/1000, y=lifeExp, size= pop, color= continent)) + 
  geom_point(shape= 16, alpha= 0.5)

# Alpha is an aesthetic to make geoms transparent, its values can range from 0 (invisible) to 1 (solid).


# Line plots/time series plots --------------------------------------------

# plot the life expectancy in the United Kingdom over time
gapdata %>% 
  filter(country == 'United Kingdom') %>%
  ggplot(aes(x= year, y= lifeExp)) +
  geom_line()


gapdata %>% 
  ggplot(aes(x= year, y= lifeExp)) +
  geom_line()

# The reason you see this weird zigzag in this Figure is that, using the above code, ggplot() does not know which points 
# to connect with which.


# you know you want a line for each country, but you haven't told it that.

gapdata %>% 
  ggplot(aes(x= year, y= lifeExp, group= country, color= continent)) + 
  geom_line() + 
  facet_wrap(~continent) + 
  scale_color_brewer(palette = 'Paired')


# Bar plots ---------------------------------------------------------------

# geom_col() and geom_bar()

# if your data is already summarised or includes values for y (height of the bars), use geom_col(). 
# If, however, you want ggplot() to count up the number of rows in your dataset, use geom_bar().

# Summarized data: 
    # - geom_col() requires two variables aes(x = , y = )
    # - x is categorical, y is continuous (numeric)

gapdata2007 %>%
  filter(country %in% c('United Kingdom', 'France', 'Germany')) %>%
  ggplot(aes(x = country, y = lifeExp)) +
  geom_col()


gapdata2007 %>%
  filter(country %in% c('United Kingdom', 'France', 'Germany')) %>%
  ggplot(aes(x = country, y = lifeExp)) +
  geom_col() +
  coord_cartesian(ylim=c(79, 81))


gapdata2007 %>% 
  ggplot(aes(x = continent)) + geom_bar()


gapdata2007 %>% 
  ggplot(aes(x= continent, color= continent)) + 
  geom_bar(fill= NA) +    # geom_bar(fill = "green"),      geom_bar(fill ="#FF0099")
  theme(legend.position = 'none')
# theme(legend.position = "none") to remove the legend (all 142 countries)

# colour vs fill
# Colour is the border around a geom, whereas fill is inside it.



#----------------------------------------------------------------------------
# Countable data

gapdata2007 %>%
  count(continent)    #  count table
                      # continent     n
                      # <fct>     <int>
                      # 1 Africa       52
                      # 2 Americas     25
                      # 3 Asia         33
                      # 4 Europe       30
                      # 5 Oceania       2


# Histograms --------------------------------------------------------------

# A histogram displays the distribution of values within a continuous variable.

gapdata2007 %>% 
  ggplot(aes(x= lifeExp)) + 
  geom_histogram(binwidth = 10)

# telling the histogram to count the observations up in "bins" of 10 years ( geom_histogram(binwidth = 10),

# There are two other geoms that are useful for plotting distributions: geom_density() and geom_freqpoly().


# Box plots ---------------------------------------------------------------

# Box plots are our go to method for quickly visualizing summary statistics of a continuous outcome variable

# - the median (middle line in the box)
# - inter-quartile range (IQR, top and bottom parts of the boxes - this is
#                       where 50% of your data is)
# - whiskers (the black lines extending to the lowest and highest values
#           that are still within 1.5*IQR)
# - outliers (any observations out with the whiskers)

gapdata2007 %>% 
  ggplot(aes(x= continent, y= lifeExp)) + 
  geom_boxplot()


# Multiple geoms, multiple aes() ------------------------------------------

gapdata2007 %>% 
  ggplot(aes(x= continent, y= lifeExp)) + 
  geom_boxplot() +
  geom_point()


# geom_point() replacing geom_jitter() - this spreads the points out to reduce over-plotting.
gapdata2007 %>% 
  ggplot(aes(x= continent, y= lifeExp, color= continent)) +
  geom_boxplot() +
  geom_jitter()



gapdata2007 %>%
  ggplot(aes(x= continent, y= lifeExp)) +
  geom_boxplot() +
  geom_jitter(aes(color= continent))
  

# Example - three geoms together ------------------------------------------

label_data <- gapdata2007 %>%
  group_by(continent) %>%
  filter(lifeExp == max(lifeExp)) %>%
  select(country, continent, lifeExp)

label_data
  
            # country   continent lifeExp
            #   <fct>     <fct>       <dbl>
            # 1 Australia Oceania      81.2
            # 2 Canada    Americas     80.7
            # 3 Iceland   Europe       81.8
            # 4 Japan     Asia         82.6
            # 5 Reunion   Africa       76.4


gapdata2007 %>% 
  ggplot(aes(x= continent, y= lifeExp)) + 
  geom_boxplot() +    #  first geom - boxplot
  geom_jitter(aes(color= continent)) +    #  second geom - jitter plot
  geom_label(data= label_data, aes(label= country))
  

# Exercise ----------------------------------------------------------------

gapminder %>% 
  ggplot(aes(x= year,
             y= lifeExp,
             group= country,
             colour= continent)) + 
  geom_line() +
  facet_wrap(~continent) +
  theme_bw() +
  scale_color_brewer(palette= 'paired')
  

# Exercise ----------------------------------------------------------------

gapminder %>%
  filter(year == 2007) %>%
  filter(continent == 'Europe') %>%    # only countries in Europe
  ggplot(aes(x= fct_reorder(country, lifeExp), y= lifeExp)) +
  geom_col(colour= 'deepskyblue', fill= NA) +
  coord_flip() +
  theme_classic()


# Extra: Advanced examples ------------------------------------------------

gapdata %>% 
  filter(continent == 'Europe') %>%
  ggplot(aes(y= fct_reorder(country, lifeExp, .fun = max),
             x= lifeExp,
             colour= year)) + 
  geom_point(shape= 15, size= 2) +
  scale_color_distiller(palette = 'Greens', direction = 1) + 
  theme_bw()


# Extra: Advanced examples ------------------------------------------------

gapdata2007 %>%
  group_by(continent) %>%
  mutate(country_number= seq_along(country)) %>%
  ggplot(aes(x= continent)) +
  geom_bar(aes(colour= continent), fill= NA, show.legend = FALSE) +
  geom_text(aes(y= country_number, label= country), vjust= 1) +
  geom_label(aes(label= continent), y= -1) +
  theme_void()

