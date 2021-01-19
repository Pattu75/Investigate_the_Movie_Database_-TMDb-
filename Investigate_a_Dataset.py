#!/usr/bin/env python
# coding: utf-8

# <a id='intro'></a>
# ## Introduction
# 
# In this project, we are going to investigate the Movie Database (TMDb), which contains information about 10,000 movies regarding to their title, release date, user ratings, as well as their budget and revenue. 
# 
# Our data analysis process for this project will provide a step by step guidance, starting by asking a series of questions, then wrangling and exploring the dataset, and finally drawing some conclusions as well as communicating the findings. 
# 
# ### Research Questions:
# 1. What are the top ten most profitables movies?
# 2. Which movie has the highest and the lowest budget?
# 3. Which movie has the highest and the lowest revenue?
# 4. In which year did movies' industry realize their most profit?
# 5. What's the relationship between both popularity and runtime of a movie against their profit?
# 6. Which movie's genre has the highest release?
# 7. Who are the most succesful directors?
# 8. What's the most frequent cast?

# In[3]:


# import all necessary core packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# The second step of our analysis is Data Wrangling, which includes assessing the TMDb Movies dataset both visually and programmatically, indentifying the presence of any tidiness issues and then improving its quality which will help us later on to analyze our data and draw conclusions.
# 
# ### General Properties

# In[4]:


# Load dataset
df = pd.read_csv('tmdb-movies.csv')
df.head(50)


# In[5]:


# view the dimension of the dataset
df.shape


# In[6]:


# Display a basic summary of the DataFrame
df.info()


# In[7]:


# check for duplicates
sum(df.duplicated())


# In[8]:


# display statistic basic summary 
df.describe()


# We can conclude from our first glimpse analysis that our dataset is dirty and messy and therefore needs to be cleaned. 
# 
# Many issues have been spotted such as:
# - Non-descriptive column headers that should be droped because they are not useful for our analysis
# - Duplicated data should be droped if any
# - Missing values or null values that should be replaced by NAN and then deleted
# - Inconsistent representations of values, dates, etc where budget and revenue should be converted into integer while release date should be converted to date format

# ### Data Cleaning (Improving Quality and Tidiness)

# After having identified the relevant issues that need to be cleaned, our second part of our data analysis process is to perform those cleaning steps:
# 
# 

# ### Step 1. Remove all unusual and non descriptive column headers:

# In[9]:


# create a list of columns to be droped from our dataset
drop_list = ['id', 'imdb_id', 'homepage', 'tagline', 'keywords', 'overview', 'production_companies', 'vote_count', 'vote_average','budget_adj', 'revenue_adj']

# drop extraneous columns from our dataset
df.drop(drop_list, axis = 1, inplace = True)
df.head(1)


# ### Step 2. Delete duplicates from our dataset:

# In[10]:


# drop duplicate data
df.drop_duplicates(inplace = True)

# confirm correction by rechecking for duplicates
sum(df.duplicated())


# ### Step 3. Check for null and missing values and remove them:

# In[11]:


# view missing value count for each feature
df.isnull().sum()


# In[12]:


# replace null values with NAN
df = df.replace(0, np.NAN)
df.head(35)


# In[13]:


# drop all NAN's rows from our dataset
df = df.dropna()
df.head(35)


# In[14]:


# recheck for missing values
df.isnull().sum()


# In[15]:


# confirm changes
df.info()


# ### Step 4. Incorrect Date format and Datatypes changes:

# In[16]:


# convert release date type from string to date format
df.release_date = pd.to_datetime(df['release_date'])
df.head(1)


# In[17]:


# convert datatypes of budget and revenue to int
df.budget = df.budget.astype(int)
df.revenue = df.revenue.astype(int)


# In[18]:


# confirm changes to the datatypes 
df.dtypes


# In[19]:


# explore our dataset
df.hist(figsize = (12,10), bins = 25)
plt.show()


# According to the plot, we can conclude that the distribution of budget, revenue, runtime and popularity are skewed to the right while the distribution of release year of movies is skewed to the left (2010 and above represents the most released movies).

# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# After having trimmed and cleaned the dataset, we are ready to move on to data exploration. So, we are going to compute statistics and create visualizations with the aim to anwer the research questions that we have posed in the introductory section. 
# 
# 
# ### Research Question 1:  What are the top ten of most profitables movies?

# #### - Calculate the profit for each movie:

# In[20]:


# add a new column called profit
df.insert(3, 'profit', df['revenue'] - df['budget'])
df.head(1)


# #### - Top ten of most profitables movies:

# In[21]:


# display the top ten movies
df.sort_values(['profit'], ascending = False).head(10)


# The famous movie "Avatar", which was directed by James Cameron and released on 2009, earned the highest profit of USD 2.5 billion from the top ten most profitable movies, and was followed by "Star Wars: The Force Awakens" that was directed by J.J Abrams with a profit of USD 1.8 billion, and then followed by "Titanic" which was directed by James Cameron with a profit of USD 1.6 billion.

# ### Research Question 2: Which movie has the highest and lowest budget ?

# In[22]:


# view the movie with the highest budget
df.loc[df['budget'].idxmax()]


# In[23]:


# display the movie with the lowest budget
df.loc[df['budget'].idxmin()]


# The movie with the highest budget spent is "The Warrior's Way" which is around 425 million, while "Lost & Found" is the movie with the lowest budget which is around $1. It should be a data entry error.

# ### Research Question 3: Which movie has the highest and the lowest revenue?

# In[24]:


# show the movie with the highest revenue
df.loc[df['revenue'].idxmax()]


# In[25]:


# show the movies with the lowest revenue
df.loc[df['revenue'].idxmin()]


# The movie with the highest revenue of 237 million is "Avatar", while "Shattered Glass" is the movie with the lowest revenue which is only $2.

# Next, let's plot respectively both the relationship between profit realized by movies and the budget spent as well as the relationship between revenue by movies and the budget spent:
# 

# In[26]:


# scatterplot of budget against profit
sns.regplot(x = df['budget'], y = df['profit'], color = 'blue')
plt.title('Budget versus Profit', fontsize = 14)
plt.show()


# In[27]:


# scatterplot of budget against revenue
sns.regplot(x = df['budget'], y = df['revenue'], color='blue')
plt.title('Budget versus Revenue', fontsize = 14)
plt.show()


# In[28]:


# create the function of correlation coefficient 
def correlation_coeff(x,y):
    std_x = (x-x.mean())/x.std(ddof=0)
    std_y = (y-y.mean())/y.std(ddof=0)
    return(std_x*std_y).mean()
correlation_coeff(df['budget'],df['profit'])


# In[29]:


correlation_coeff(df['budget'],df['revenue'])


# Both budget and profit and also budget and revenue have a positive correlation of 0.53 and 0.68 respectively which means that the more budget spent on a movie the more revenue or profit to be realized. However, according to the both plot we can highlight that some movies earned a high profit with less budget spent. 

# ### Research Question 4: In which year did movies' industry realize their most profit?

# In[30]:


# get total profit made by release_year
profit_year = df.groupby('release_year')['profit'].sum()
profit_year.head()


# In[31]:


# plot profit made for each realeased year
profit_year.plot(figsize = (10,8), color = 'b')
plt.xlabel('Year', fontsize = 12)
plt.ylabel('Profit', fontsize = 12 )
plt.title('Profit made for each released year', fontsize = 14)
plt.show()


# The relationship between Total profit and released year is upward trending, which means that in recent years particularly after 2010, the movies' indutry realized the greatest profit about USD 20 billion (2 times 1e10 million) compared to the period between 1960 and 2005 where the profit didn't go beyond USD 10 billion. 
# 
# Next, we are going to identify whether the yearly realized total profit is due the popularity of both old and new movies or only due to the highest rate of released of new movies in a year. 

# ### Research Question 5: What's the relationship between both popularity, runtime of a movie and their profit?

# In[32]:


# scatterplot of popularity against profit
# scatterplot of runtime against profit
sns.pairplot(df, x_vars =['popularity', 'runtime'], y_vars = ['profit'], size = 7, aspect = 0.7, kind='reg')
plt.title('The effect of Popularity and Runtime on Profit', fontsize = 14)
plt.show()


# In this section, we are trying to find out how popularity and runtime affect profit. 
# 
# According to both scatterplots, we can conclude that the trendline in both of them is upward sloping, and  there is a positive relationship not only between popularity and profit but also between runtime and profit. This means that both higher popularity and runtime increase profit. In addition, the slope of popularity is greater than the slope of runtime which means that profit increased with a higher rate with popularity that did with runtime.
# 
# Let's check by how much profit is affected by both popularity and runtime by calculating the correlation coefficient:

# In[33]:


# create the function of correlation coefficient 
def correlation_coeff(x,y):
    std_x = (x-x.mean())/x.std(ddof=0)
    std_y = (y-y.mean())/y.std(ddof=0)
    return(std_x*std_y).mean()


# In[34]:


# correlation between popularity and profit
correlation_coeff(df['popularity'], df['profit'])


# In[35]:


# correlation between runtime and profit
correlation_coeff(df['runtime'], df['profit'])


# The coefficient of correlation between popularity and profit is positive and it is around 0.60 which means that a movie with high popularity rate tends to earn higher profit. While the lower coefficient of correlation between runtime and profit of 0.14 means that the longer the duration of a movie the less higher the profit.

# In[36]:


df['runtime'].describe()


# In addition, it can be inferred from the runtime plot and from the above statistic description that some movies in the runtime range between 95 and 120 tends to earn higher profit: 
# - 25% of movies have runtime less than 95mn
# - 50% of movies have a runtime less than 106mn which is the median of the runtime distribution.
# - 75% of movies have a runtime less than 119mn
# - The mean is 109 which is higher than the median of 106 which means that the runtime distribution is skewed to the right.
# So, the audience prefer better a movie with a runtime that falls on the range.

# ### Research Question 6: Which movie's genre has the highest release? 

# In[37]:


df.head(1)


# The below built-in function will help us to separate the content of genre features and then count the number of the movies corresponding to each genre:

# In[38]:


# create a function that separate the content of genres
def count_genre(column):
    split_data = pd.Series(df[column].str.cat(sep='|'). split('|'))
    count_data = split_data.value_counts(ascending = False)
    return count_data


# In[39]:


# count realized movies by genres
count_data = count_genre('genres')
count_data.head()


# In[40]:


# plot genres against released movies
count_data.plot(kind ='barh', figsize = (14,8), fontsize = 12)
plt.xlabel('Number of movies', fontsize = 12)
plt.ylabel('Genres', fontsize = 12)
plt.title('Genres with the highest release', fontsize = 14)
plt.show()


# According to the plot, we can conclude that the audience prefer the most Drama, after that they prefer watching Comedy's movies, then Thriller as well as Action's movies. All of them represent the highest proportion of profit for the movies' industry. The highest the preference rate for those genres, the greatest corresponding released movies and therefore the highest profit. 

# ### Research Question 7: Who are the most succesful directors?

# In this section, we are going to check who is the succesful director that directed the maximum number of movies.

# In[41]:


# create a built-in function that count movies by director
def count_director_movies(column):
    split_data = pd.Series(df[column].str.cat(sep='|'). split('|'))
    count_data = split_data.value_counts(ascending = False)
    return count_data


# In[42]:


# display the top ten best director
count_data = count_director_movies('director')
count_data.head(10)


# Steven Spielberg is the most prolific American director with 28 movies to his credit, followed by Clint Eastwood with 24 movies, Ridley Scott with 21 and then Martin Scorsese with 17 filmes in his credit.

# ### Research Question 8: What's the most frequent cast?

# In[43]:


# create a built-in function 
def count_cast_movies(column):
    split_data = pd.Series(df[column].str.cat(sep='|'). split('|'))
    count_data = split_data.value_counts(ascending = False)
    return count_data


# In[44]:


# display the most frequent cast
count_data = count_cast_movies('cast')
count_data.head(10)


# A good actor in a movie like Robert De Niro or Bruce Willis and others is a sign of a good casting and definitely a good sign for a successful movie in terms of audience and profit. The mean reason is that a a good casting do a great job in portraying very well their characters.  

# <a id='conclusions'></a>
# ## Conclusions
# 
# For the sake of summary, the following are the findings of investigating the Movie Database (TMDb):
# - "Avatar", "Star Wars: The Force Awakens" and "Titanic" are the most profitable movies.
# - "Avatar" is the movie with the highest revenue, while "Shattered Glass" is the movie with the lowest revenue.
# - The "Warrior's Way" is the movie with the highest budget spent.
# - There is a strong relationship between budget and revenue explained by a positive correlation of 0.68 which means that an increase in budget allocated to a movie leads to an increase in its revenue.
# - There is also a strong relationship between budget and profit which is explained by a positive correlation of 0.53. However, we have to mention that some movies earned higher profit with less spendings. 
# - After 2010, the movies' indutry realized the greatest profit about USD 20 billion compared to the period between 1960 and 2005 where the profit didn't go beyond usd 10 billion.
# - There is a positive relationship between popularity and profit where the coefficient of correlation is around 0.60 which is high and explain why higher movie's popularity increase profit with a higher value. 
# - There is also a positive relationship between runtime and profit where the coefficient of correlation is only around 0.14 which means the profit is increased with lower value with longer duration of a movie. The skewness to the right of the runtime scatterplot makes us to conclude that movies in the runtime range between 95 and 120 tends to earn higher profit.
# - Drama, followed by Comedy, Thriller and Action are the most preferable movies' genres by the audience.
# - Steven Spielberg is the most successful director with 28 movies to his credit, while the best actor comes back to Robert De Niro with 52 movies.
# 
# One of the limitations to draw perfect conclusion is that a poorer quality of the database can potentially be costing higher price to the final findings. The database was untidy, may be because the data was collected from various sources, the reason why there were many null and missing values. Morever, our dataset should be cleaned and assessed before being analyzed which leads that many movies where exluded from our analysis.
# 
# 
# 
# ## Submitting your Project 
# 
# 

# In[1]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])


# In[ ]:




