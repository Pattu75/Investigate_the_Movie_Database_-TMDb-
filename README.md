# Investigate_the_Movie_Database_-TMDb-

# Table of Contents:

* Introduction
* Data Wrangling
* Exploratory Data Analysis
* Conclusions

# Introduction:
In this project, we are going to investigate the Movie Database (TMDb), which contains information about 10,000 movies regarding to their title, release date, user ratings, as well as their budget and revenue.

Our data analysis process for this project will provide a step by step guidance, starting by asking a series of questions, then wrangling and exploring the dataset, and finally drawing some conclusions as well as communicating the findings.

## Research Questions:
1. What are the top ten most profitables movies?
2. Which movie has the highest and the lowest budget?
3. Which movie has the highest and the lowest revenue?
4. In which year did movies' industry realize their most profit?
5. What's the relationship between both popularity and runtime of a movie against their profit?
6. Which movie's genre has the highest release?
7. Who are the most succesful directors?
8. What's the most frequent cast?

# Data Wrangling:
The second step of our analysis is Data Wrangling, which includes assessing the TMDb Movies dataset both visually and programmatically, indentifying the presence of any tidiness issues and then improving its quality which will help us later on to analyze our data and draw conclusions.

## Data Cleaning (Improving Quality and Tidiness):
After having identified the relevant issues that need to be cleaned, our second part of our data analysis process is to perform those cleaning steps:

* Step 1. Remove all unusual and non descriptive column headers
* Step 2. Delete duplicates from our dataset
* Step 3. Check for null and missing values and remove them
* Step 4. Incorrect Date format and Datatypes changes

# Exploratory Data Analysis:
After having trimmed and cleaned the dataset, we are ready to move on to data exploration. So, we are going to compute statistics and create visualizations with the aim to anwer the research questions that we have posed in the introductory section.

# Conclusions:
For the sake of summary, the following are the findings of investigating the Movie Database (TMDb):

* "Avatar", "Star Wars: The Force Awakens" and "Titanic" are the most profitable movies.
* "Avatar" is the movie with the highest revenue, while "Shattered Glass" is the movie with the lowest revenue.
* The "Warrior's Way" is the movie with the highest budget spent.
* There is a strong relationship between budget and revenue explained by a positive correlation of 0.68 which means that an increase in budget allocated to a movie leads to an increase in its revenue.
* There is also a strong relationship between budget and profit which is explained by a positive correlation of 0.53. However, we have to mention that some movies earned higher profit with less spendings.
* After 2010, the movies' indutry realized the greatest profit about USD 20 billion compared to the period between 1960 and 2005 where the profit didn't go beyond usd 10 billion.
* There is a positive relationship between popularity and profit where the coefficient of correlation is around 0.60 which is high and explain why higher movie's popularity increase profit with a higher value.
* There is also a positive relationship between runtime and profit where the coefficient of correlation is only around 0.14 which means the profit is increased with lower value with longer duration of a movie. The skewness to the right of the runtime scatterplot makes us to conclude that movies in the runtime range between 95 and 120 tends to earn higher profit.
* Drama, followed by Comedy, Thriller and Action are the most preferable movies' genres by the audience.
* Steven Spielberg is the most successful director with 28 movies to his credit, while the best actor comes back to Robert De Niro with 52 movies.

One of the limitations to draw perfect conclusion is that a poorer quality of the database can potentially be costing higher price to the final findings. The database was untidy, may be because the data was collected from various sources, the reason why there were many null and missing values. Morever, our dataset should be cleaned and assessed before being analyzed which leads that many movies where exluded from our analysis.
