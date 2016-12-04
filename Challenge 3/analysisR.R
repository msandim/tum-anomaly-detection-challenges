library(dplyr)
library(ggplot2)

feat <- read.csv("features.csv")
train <- read.csv("training-set.csv")
test <- read.csv("testing-set.csv")

ggplot(train, aes(factor(label), dur)) +
  geom_boxplot() +
  geom_jitter(width = 0.3)

ggplot(train, aes(factor(label), sbytes)) +
  geom_boxplot() +
  geom_jitter(width = 0.3)

ggplot(train[train$label != 0,], aes(factor(label))) +
  geom_bar() +
  facet_grid(~state)