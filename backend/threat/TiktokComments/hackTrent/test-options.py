import json 
import pandas as pd
from textblob import TextBlob
import nltk

# Function that loads json data
def load_data(json_path):
    # Open the JSON file in read mode
    with open(json_path, 'r') as file:
        # Load the JSON data into a Python dictionary or list (depending on JSON structure)
        data = json.load(file)
    # Convert the loaded JSON data to a pandas DataFrame for easier manipulation
    return pd.DataFrame(data)


# Load the Reddit comments CSV file using the full path
# comments_df = pd.read_csv('/Users/saeidk/Downloads/reddit_comments_cleaned.csv')

# Function to classify sentiment using TextBlob
def classify_sentiment(text):
    try:
        # Get the polarity score using TextBlob
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        # Classify sentiment based on polarity score
        if polarity > 0:
            return "positive", polarity
        elif polarity < 0:
            return "negative", polarity
        else:
            return "neutral", polarity
    except Exception as e:
        print(f"Error processing comment: {e}")
        return "error", 0.0


json_path = 'comments.json'
comments = load_data(json_path)

# Apply the sentiment classifier to each comment
# comments['Sentiment'], comments['Polarity'] = zip(*comments['Comment'].apply(classify_sentiment))

comments[['Sentiment', 'Polarity']] = comments['comment'].apply(lambda text: pd.Series(classify_sentiment(text)))


# Save the results to a new CSV file
# comments_df.to_csv('/Users/saeidk/Downloads/reddit_comments_with_sentiment.csv', index=False)

print(comments)

# print("Sentiment analysis completed and results saved to '/Users/saeidk/Downloads/reddit_comments_with_sentiment.csv'")
