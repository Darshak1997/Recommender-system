# -*- coding: utf-8 -*-
"""
Created on Mon May 20 12:23:31 2019

@author: Darshak
"""
#%matplotlib inline
import numpy as np
import pandas as pd

column_name = ['user_id', 'item_id', 'rating', 'timestamp']
df = pd.read_csv('u.data.csv', sep = '\t', names = column_name)
df.head()

movie_titles = pd.read_csv('movie_id_title.txt')
movie_titles.head()

df = pd.merge(df, movie_titles, on = 'item_id')
df.head()

import matplotlib.pyplot as plt
import seaborn as sns


sns.set_style('white')
df.groupby('title')['rating'].mean().sort_values(ascending = False).head(10)

df.groupby('title')['rating'].count().sort_values(ascending = False).head(10)

ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.head()

ratings['rating_numbers'] = pd.DataFrame(df.groupby('title')['rating'].count())
ratings.head()

ratings['rating_numbers'].hist(bins = 50)
ratings['rating'].hist(bins = 50)

sns.jointplot(x = 'rating', y = 'rating_numbers', data = ratings, alpha = 0.5)

moviemat = df.pivot_table(index = 'user_id', columns = 'title', values = 'rating')
moviemat.head()

ratings.sort_values('rating_numbers', ascending = False).head(10)


starwars_user_ratings = moviemat['Star Wars (1977)']
liar_liar_user_ratings =moviemat['Liar Liar (1997)']
starwars_user_ratings.head()

similar_to_starwars = moviemat.corrwith(starwars_user_ratings)
similar_to_starwars.head()

similar_to_liarliar = moviemat.corrwith(liar_liar_user_ratings)
similar_to_liarliar.head()


corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()

corr_starwars.sort_values('Correlation', ascending=False).head(10)

corr_starwars = corr_starwars.join(ratings['rating_numbers'], how='left', lsuffix='_left', rsuffix='_right')
corr_starwars.head()

corr_starwars[corr_starwars['rating_numbers']>100].sort_values('Correlation', ascending=False).head()

corr_liarliar = pd.DataFrame(similar_to_liarliar, columns=['Correlation'])
corr_liarliar.head()

corr_liarliar.dropna(inplace=True)
corr_liarliar = corr_liarliar.join(ratings['rating_numbers'], how='left')
corr_liarliar.head()

corr_liarliar[corr_liarliar['rating_numbers']>100].sort_values('Correlation', ascending=False).head()

# GENERALIZED VERSION
movie_name = raw_input("Which movie would you like to watch?")
general_user_ratings = moviemat[movie_name]
general_user_ratings.head()

similar_to_your_movie = moviemat.corrwith(general_user_ratings)
similar_to_your_movie.head()

corr_your_movie = pd.DataFrame(similar_to_your_movie, columns = ['Correlation'])
corr_your_movie.dropna(inplace = True)
corr_your_movie.head()

corr_your_movie.sort_values('Correlation', ascending = False).head(10)
corr_your_movie = corr_your_movie.join(ratings['rating_numbers'], how = 'left', lsuffix = '_left', rsuffix = '_right')
corr_your_movie.head()

corr_your_movie[corr_your_movie['rating_numbers']>100].sort_values('Correlation', ascending=False).head()