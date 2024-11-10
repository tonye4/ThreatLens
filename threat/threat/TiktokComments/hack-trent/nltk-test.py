# Identify Hurtful Phrases in Comments

# install nltk
import nltk
nltk.download('vader_lexicon')

# import required libraries
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# analyze Sentiment
# polarity_scores() method analyzes text sentiment
# returns a dictionary with scores for positive, neutral, negative, and compound sentiment values
def analyze_sentiment(text):
    score = sia.polarity_scores(text)
    compound = score['compound']
    sentiment = ""
    if compound >= 0.05:
        sentiment = "Positive"
        return "Positive"
    elif compound <= -0.05:
        sentiment = "Negative"
        return "Negative"
    else:
        sentiment = "Neutral"
        return "Neutral"
    
print(analyze_sentiment("awesome movie"))