
# Exporting and reporting -------------------------------------------------

library(tidyverse)
library(finalfit)
# Specify explanatory variables of interest
explanatory <- c("age", "sex.factor", "extent.factor", "obstruct.factor","nodes")
colon_s %>%
  summary_factorlist("differ.factor", explanatory,
                     p=TRUE, na_include=TRUE)



colon_s <- colon_s %>%
  mutate(
    nodes = ff_label(nodes, "Lymph nodes involved")
  )
table1 <- colon_s %>%
  summary_factorlist("differ.factor", explanatory,
                     p=TRUE, na_include=TRUE,
                     add_dependent_label=TRUE,
                     dependent_label_prefix = "Exposure: "
  )
table1



# Logistic regression table -----------------------------------------------

# After investigating the relationships between our explanatory variables, we will use logistic regression to include the outcome variable.

explanatory <- c( "differ.factor", "age", "sex.factor", "extent.factor", "obstruct.factor", "nodes")
dependent <- "mort_5yr"

table2 <- colon_s %>%
  finalfit(dependent, explanatory,
           dependent_label_prefix = "")
table2



# Odds ratio plot ---------------------------------------------------------

colon_s %>%
  or_plot(dependent, explanatory,
          breaks = c(0.5, 1, 5, 10, 20, 30),
          table_text_size = 3.5)


# MS Word via knitr/R Markdown --------------------------------------------

# Save objects for knitr/markdown
# install.packages('here')
save(table1, table2, dependent, explanatory, file = here::here("data", "out.rda"))

# In RStudio, select: File  ->  New File -> R Markdown


# Figure quality in Word output -------------------------------------------

knitr::opts_chunk$set(dpi = 300)


# Create Word template file -----------------------------------------------

# ---
#   title: "Example knitr/R Markdown document"
# author: "Your name"
# date: "22/5/2020"
# output:
#   word_document:
#   reference_docx: colonTemplate.docx
# ---
#   ```{r setup, include=FALSE}
# # Load data into global environment.
# library(finalfit)
# library(dplyr)
# library(knitr)
# load(here::here("data", "out.rda"))
# ```
# ## Table 1 - Demographics
# ```{r table1, echo = FALSE}
# kable(table1, row.names=FALSE, align=c("l", "l", "r", "r", "r",  "r"))
# ```
# ## Table 2 - Association between tumour factors and 5 year
# mortality
# ```{r table2, echo = FALSE}
# kable(table2, row.names=FALSE, align=c("l", "l", "r", "r", "r", "r"))
# 
# ## Figure 1 - Association between tumour factors and 5 year
# mortality
# ```{r figure1, echo=FALSE, message=FALSE, warning=FALSE,
# fig.width=10}
# explanatory = c( "differ.factor", "age", "sex.factor",
#                  "extent.factor", "obstruct.factor",
#                  "nodes")
# dependent = "mort_5yr"
# colon_s %>%
#   or_plot(dependent, explanatory,
#           breaks = c(0.5, 1, 5, 10, 20, 30))
# ```


# PDF via knitr/R Markdown ------------------------------------------------

# library(dplyr)
# library(knitr)
# library(kableExtra)
# load(here::here("data", "out.rda"))
# ```
# ## Table 1 - Demographics
# ```{r table1, echo = FALSE}
# kable(table1, row.names=FALSE, align=c("l", "l", "r", "r", "r",
#                                        "r"),
#       booktabs = TRUE)
# ```
# ## Table 2 - Association between tumour factors and 5 year
# mortality
# ```{r table2, echo = FALSE}
# kable(table2, row.names=FALSE, align=c("l", "l", "r", "r", "r",
#                                        "r"),
#       booktabs=TRUE) %>%
#   kable_styling(font_size=8)
# ```
# ## Figure 1 - Association between tumour factors and 5 year
# mortality
# ```{r figure1, echo=FALSE, message=FALSE, warning=FALSE,
# fig.width=10}
# explanatory = c( "differ.factor", "age", "sex.factor",
#                  "extent.factor", "obstruct.factor",
#                  "nodes")
# dependent = "mort_5yr"
# colon_s %>%
#   or_plot(dependent, explanatory,
#           breaks = c(0.5, 1, 5, 10, 20, 30))
# ```