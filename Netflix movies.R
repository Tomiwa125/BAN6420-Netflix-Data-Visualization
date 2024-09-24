library(ggplot2)


df <- read.csv("C://Users//Beacon Consulting//Downloads//Netflix.py//Netflix_shows_movies//netflix_data.csv")

ggplot(df, aes(x=rating)) +
    geom_bar() +
    labs(title="Ratings Distribution", x="Ratings", y="Count") +
    theme_minimal()