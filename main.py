import praw
import pandas as pd
import textacy as textacy
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
import string
from nltk.sentiment import SentimentIntensityAnalyzer
import seaborn as sns
import matplotlib.pyplot as plt
from wordcloud import WordCloud



# STAGE 1: Data extraction

reddit = praw.Reddit(
    client_id="Your ID",
    client_secret="Your secret",
    user_agent="Your user agent"
)

subreddit_name = "news"

subreddit = reddit.subreddit(subreddit_name)
posts = subreddit.top(limit=100)

post_data = []

for post in posts:
    title = post.title
    description = post.url
    creation_date = pd.to_datetime(post.created_utc, unit="s")
    author = post.author.name if post.author else "Brak"
    upvotes = post.score

    post_data.append(
        {"Title": title, "Description": description, "Creation Date": creation_date, "Author": author, "Upvotes": upvotes})

df = pd.DataFrame(post_data)

df.to_csv("posts.csv", index=False)



# STAGE 2: Text Processing

stop_words = set(stopwords.words("english"))

def process_text(text):
    if pd.isnull(text):
        return ""
    text = str(text).lower()
    text = "".join([c for c in text if c.isalnum() or c.isspace()])
    tokens = word_tokenize(text)
    tokens = [token for token in tokens if token not in stop_words and token not in string.punctuation]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    processed_text = " ".join(tokens)
    return processed_text

df["Processed Titles"] = df["Title"].apply(process_text)



# STAGE 3: Keyword Extraction

keywords = []

for title in df["Processed Titles"]:
    doc = textacy.make_spacy_doc(title, lang="en_core_web_sm")
    doc_keywords = textacy.extract.keyterms.sgrank(doc, ngrams=(1, 2, 3), normalize="lower", topn=5)
    keywords.append([keyword for keyword, _ in doc_keywords])



# STAGE 4: Sentiment Analysis

keyword_sentiments = []

sia = SentimentIntensityAnalyzer()

for topic_keywords in keywords:
    sentiment_scores = [sia.polarity_scores(keyword)["compound"] for keyword in topic_keywords]
    if sentiment_scores:
        average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
        sentiment_label = "positive" if average_sentiment >= 0 else "negative"
    else:
        average_sentiment = 0
        sentiment_label = "neutral"
    keyword_sentiments.append(sentiment_label)

df["Keyword Sentiment Analysis"] = keyword_sentiments

df.to_csv("posts2.csv", index=False)



# STAGE 5: Visualization of Sentiment Analysis

colors = {"positive": "#669900", "negative": "#c65353", "neutral": "#c2c2d6"}

ax = sns.countplot(data=df, x="Keyword Sentiment Analysis", palette=colors.values(), hue="Keyword Sentiment Analysis", legend=False)

tick_positions = [0, 1, 2]
tick_labels = ['Positive', 'Negative', 'Neutral']

ax.set_xticks(tick_positions)
ax.set_xticklabels(tick_labels)

plt.title("Keyword Sentiment Analysis")
plt.xlabel("Sentiment")
plt.ylabel("Count")

total_count = len(df)
for p in ax.patches:
    count = p.get_height()
    ax.annotate(f"{int(count)}", (p.get_x() + p.get_width() / 2, p.get_height()), ha="center", va="center")

plt.show()



# STAGE 6: Visualization of Extracted Keywords Using Word Cloud
combined_keywords = " ".join([keyword for keyword_list in keywords for keyword in keyword_list])

remove_u = [keyword for keyword in combined_keywords.split() if keyword != "u"]

word_cloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(remove_u))

plt.figure(figsize=(10, 6))
plt.imshow(word_cloud, interpolation="bilinear")
plt.title("Keyword Word Cloud of subreddit r/news")
plt.axis("off")
plt.show()
