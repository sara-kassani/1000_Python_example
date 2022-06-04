
# Fine tuning plots -------------------------------------------------------

library(tidyverse)
library(gapminder)

p0 <- gapminder %>%
  filter(year == 2007) %>%
  ggplot(aes(y= lifeExp, x= gdpPercap, color= continent)) + 
  geom_point(alpha= 0.3) +
  theme_bw() +
  geom_smooth(method = 'lm', se= FALSE) +
  scale_color_brewer(palette = 'Set1')


p0


# Scales ------------------------------------------------------------------

# Logarithmic ---------------
p1 <- p0 + scale_x_log10()


# Expand limits -----------------------------------------------------------

# A quick way to expand the limits of your plot is to specify the value you want to be included
p2 <- p0 + expand_limits(y = 0)

# Or two values for extending to both sides of the plot:
p3 <- p0 + expand_limits(y= c(0, 100))

# By default, ggplot() adds some padding around the included area. This ensures points on the edges don't get overlapped with the axes, 
# but in some cases - especially if you've already expanded the scale, you might want to remove this extra padding. You can remove 
# this padding with the expand argument.

p4 <- p0 + expand_limits(y= c(0, 100)) +
  coord_cartesian(expand= FALSE)


# library - patchwork - to print all 4 plots together

library(patchwork)
# install.packages('patchwork')

p1 + p2 + p3 + p4 + plot_annotation(tag_levels = '1', tag_prefix = 'p')


# p1: Using a logarithmic scale for the x axis. p2: Expanding the limits of the y axis to include 0. p3: Expanding the limits of 
# the y axis to include 0 and 100. p4: Removing extra padding around the limits.


# Zoom in -----------------------------------------------------------------

p5 <- p0 +
  coord_cartesian(ylim = c(70, 85), xlim = c(20000, 40000))


p6 <- p0 +
  scale_y_continuous(limits = c(70, 85)) +
  scale_x_continuous(limits = c(20000, 40000))

p5 + labs(tag = 'p5') + p6 +labs(tag = 'p6')


# Axis ticks --------------------------------------------------------------

# calculating the maximum value to be included in the axis breaks:
max_value <- gapminder %>% 
  filter(year == 2007) %>%
  summarise(max_lifeExp = max(lifeExp)) %>%
  pull(max_lifeExp) %>% 
  round(1)

# using y_Scale_continuous(breaks= ...):
p7 <- p0 +
  coord_cartesian(ylim = c(0, 100), expand = 0) + 
  scale_y_continuous(breaks = c(18, 50, max_value))


p8 <- p0 +
  coord_cartesian(ylim = c(0, 100), expand = 0) + 
  scale_y_continuous(breaks = c(18, 50, max_value), labels = c('Adults', '50', 'MAX'))


p7 + labs(tag= 'p7') + p8 + labs(tag = 'p8')



# Colors -----------------------------------------------------------------

# Using the Brewer palettes: ----------------------------------------------

# The easiest way to change the colour palette of your ggplot() is to specify a Brewer palette.

p9 <- p0 +
  scale_color_brewer(palette = 'Paired')


# Legend title ------------------------------------------------------------

# scale_colour_brewer() is also a convenient place to change the legend title

p10 <- p0 +
  scale_color_brewer("Continent - \n one of 5", palette = 'Paired')

p9 + labs(tag = 'p9') + p10 + labs(tag = 'p10')


# Choosing colours manually -----------------------------------------------

p11 <- p0 +
  scale_color_manual(values = c('red', 'green', 'blue', 'purple', 'pink'))


p12 <- p0 +
  scale_color_manual(values = c("#8dd3c7", "#ffffb3", "#bebada", "#fb8072", "#80b1d3"))


p11 + labs(tag = 'p11') + p12 + labs(tag = 'p12')


# Titles and labels -------------------------------------------------------

# We've been using the labs(tag = ) function to add tags to plots. But the labs() function can also be used to modify axis labels, 
# or to add a title, subtitle, or a caption to your plot

p13 <- p0 +
  labs(x = 'Gross domestic product per capita', 
       y = 'Life expectancy',
       title = 'Health and economics',
       subtitle = 'Gapminder dataset, 2007',
       caption = Sys.Date(),
       tag = "p13")
p13


# Annotation --------------------------------------------------------------
# For 'hand' annotating a plot, use the annotate() function.

p14 <- p0 +
  annotate("text",
           x= 25000,
           y= 50,
           label= 'No points here!')

p14


p15 <- p0 +
  annotate("label",
           x= 25000,
           y= 50,
           label= 'No points here!')


p15


p16 <- p0 +
  annotate("label",
           x= 25000,
           y= 50,
           label= 'No points here!',
           hjust= 0)

p16



p14 + labs(tag = "p14") + (p15 + labs(tag = "p15"))/ (p16 + labs(tag = "p16"))



# Annotation with a superscript and a variable ----------------------------

fit_glance <- tibble(r.squared = 0.7693465)
plot_rsquared <- paste0(
  "R^2 == ",
  fit_glance$r.squared %>% round(2))
p17 <- p0 +
  annotate("text",
           x = 25000,
           y = 50,
           label = plot_rsquared, parse = TRUE,
           hjust = 0)
p17 + labs(tag = "p17")


# Text size --------------------------------------------------

p18 <- p0 +
  theme(axis.text.y = element_text(colour = "green", size = 14),
        axis.text.x = element_text(colour = "red", angle = 45, vjust = 0.5),
        axis.title = element_text(colour = "blue", size = 16))
p18 + labs(tag = "p18")


# Legend position ---------------------------------------------------------

p19 <- p0 +
  theme(legend.position = "none")

p20 <- p0 +
  theme(legend.position = c(1,0), #bottom-right corner
        legend.justification = c(1,0))

p19 + labs(tag = "p19") + p20 + labs(tag = "p20")


p21 <- p0 +
  guides(colour = guide_legend(ncol = 2)) +
  theme(legend.position = "top") # moving to the top optional
p21 + labs(tag = "p21")


# Saving your plot --------------------------------------------------------
ggsave(p0, file = "my_saved_plot.pdf", width = 5, height = 4)



