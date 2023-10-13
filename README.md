# Keyword extraction and analysis from the r/news subreddit

This project employs NLP to extract and analyze top posts from Reddit's r/news subreddit, focusing on keyword extraction and sentiment analysis. It provides insights into popular news topics, keywords, and their sentiments within the community.

## Table of Contents
1. [Project Goal](#goal)
2. [Build With](#build)
3. [Project Description](#description)
4. [The Results](#results)

<a name="goal"></a>
### 1. Project Goal

The aim of the project is to develop a program that will use natural language processing techniques to extract and analyze top posts from the r/news subreddit on the reddit.com platform (https://www.reddit.com/r/news/). The selected subreddit is one of the most popular on the platform and focuses on news from around the world. 

The project focuses on extracting keywords from post titles, conducting sentiment analysis on the extracted keywords and visualizing the results. This makes it possible to research and understand the most frequently discussed news, identify the most important keywords in this community and determine their sentiment.


<a name="build"></a>
### 2. Build With

* Python
* praw
* pandas
* textacy
* nltk
* seaborn
* matplotlib
* wordcloud
* spaCy
* networkx


<a name="description"></a>
### 3. Project Description

The project includes the analysis of top posts from the r/news subreddit and consists of the following stages:

1. **Data extraction**: accessing the Reddit API, downloading posts from the TOP category and saving them to a CSV file.
2. **Text processing**: pre-processing of post titles (converting uppercase letters to lowercase letters, removing punctuation marks and interludes, and lemmatizing tokens).
3. **Keyword Extraction**: Keyword extraction using the TextRank algorithm from the TextaCy library.
4. **Sentiment analysis**: performing sentiment analysis using the VADER module from the NLTK library, i.e. assigning a sentiment score for keywords (positive, negative, or neutral).
5. **Sentiment analysis visualization**: made using a bar chart.
6. **Visualization of the obtained keywords**: made using a word cloud.

<a name="results"></a>
### 4. The Results 

Among the top 100 titles from the r/news subreddit, our analysis revealed that 63% were associated with positive sentiments, 33% with negative sentiments, and 4% were categorized as neutral. This observation suggests a prevailing positive sentiment among the titles, indicating that the subreddit's top posts tend to convey a predominantly positive tone.

![sentiments](https://github.com/abrylanska/reddit-text-analysis-sentiment-visualization/assets/58529933/72a7d244-55df-47af-8d78-83194b388700)



The most frequently appearing words were, for example: _police_, _trump_, _biden_, _murder_ or _president_:

![wordcloud](https://github.com/abrylanska/reddit-text-analysis-sentiment-visualization/assets/58529933/2c5534a4-f61a-45d8-ab4e-f8bb99817da4)
