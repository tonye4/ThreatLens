# Detect Threat in User Account Comments

import json 
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re  # To help with tokenization and text cleaning
import codecs #to read unicode from a file
from potentially_harmful_emojis import hamrful_emojis

from nltk.corpus import stopwords
from nltk.tokenize.regexp import regexp_tokenize #using regexp to quickly search through text
from multiprocessing import Pool  #using pool to create faster lemmatization (https://stackoverflow.com/questions/38019823/faster-lemmatization-techniques-in-python)

import emoji

# Set display options for Pandas
pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
pd.set_option('display.width', None)  # Automatically adjust width
pd.set_option('display.max_colwidth', None)  # Show full content in each column
   
# Function that loads json data and flattens it
def load_data(json_path):
    # Open the JSON file in read mode
    with open(json_path, 'r', encoding='utf-8') as file:
        # Load the JSON data into a Python dictionary or list (depending on JSON structure)
        data = json.load(file)

    # Flatten the JSON data to extract individual comments
    comments_list = []
    for post in data:
        post_url = post['post_url']  # Extract the post URL for context
        for comment in post['comments']:
            username = comment.get('name')  # Extract the username (if available)
            comment_text = comment.get('comment')  # Extract the comment text
            if username and comment_text:
                comments_list.append({
                    'post_url': post_url,
                    'username': username,
                    'comment': comment_text
                })

    # Convert the flattened list into a pandas DataFrame for easier manipulation
    return pd.DataFrame(comments_list)

# Function to read txt file
def get_harmful_keywords():
    with open('potentially_harmful_words.txt', 'r') as file:
        # Read each line, strip whitespace, and create a list of words
        harmful_keywords = [line.strip() for line in file]
        return harmful_keywords

# Initialize sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Function that analyzes sentiment and flags potentially harmful comments
def sentiment_analysis(text):
    score = sia.polarity_scores(text)
    # Extract how likely it is for a comment to be negative
    # print(score)
    neg_score = score['neg']
    # Determine sentiment category
    sentiment_category = "Harmful" if score['neg'] > (score['pos'] + score['neu'])/2 else "Non-Harmful"
    return neg_score, sentiment_category
    
# Function to count harmful words using profanity-check
# keyword matching
def keywords_analysis(text):
    harmful_keywords = get_harmful_keywords()  # List of harmful words/phrases
    # findall finds all matches of the pattern within the text.
    # pattern \b\w+\b splits the text into individual words
    # words will store a list containing the comment words
    words = re.findall(r'\b\w+\b', text.lower())
    # calculates the number of harmful words found in text
    harmful_words_count = sum(1 for word in words if word in harmful_keywords)
    return harmful_words_count 

#opening text file of emoji unicode
def load_emojis(path):
    with codecs.open(path, "r", encoding="utf-8") as file:
        emojis = file.read().strip().split()  # Splitting to treat each emoji as an individual entry
    return emojis # returns the emojis as a string

# Function to get count of the number of potentially harmful emojis
def emojis_analysis(text, path="potentially_harmful_emojis.txt"):  
    harmful_emojis = set(load_emojis(path))  # Use a set for quicker lookup
    harmful_emoji_count = 0
    for char in text:
        if char in harmful_emojis:
            harmful_emoji_count += 1
            # print(f"Found harmful emoji: {char}")  # Debugging line to confirm matching emojis
        # else:
            # print(f"Non-harmful or unrecognized emoji: {char}")  # For tracking mismatches
    return harmful_emoji_count


# Wrapper Function to Identify harmful comments    
# Function to detect harmful comments
def comments_analysis(json_path):
    # load the data from the json file
    comments = load_data(json_path)
    # sentiment analysis: How likely it is for the comment to be negative, sentiment category (based on negative score)
    comments[['Negative Probability', 'Sentiment Category']] = comments['comment'].apply(lambda text: pd.Series(sentiment_analysis(text)))
    # keyword matching: count number of offensive words in a comment
    comments['Harmful Words Count'] = comments['comment'].apply(keywords_analysis)
    comments['Harmful Emoji Count'] = comments['comment'].apply(emojis_analysis)     
    return comments


# Reputation score: assigned to users based on their past behavior (e.g., number of harmful comments flagged over time).
# Modify to take more things into consideration
def get_reputation_score(analyzed_comments):
    # Dictionary to store cumulative reputation scores by username
    user_reputation_scores = {}
    
    for index, row in analyzed_comments.iterrows():
        # Access each field in the row using row['column_name']
        username = row['username']
        comment = row['comment']
        negative_probability = row['Negative Probability']
        sentiment_category = row['Sentiment Category']
        harmful_words_count = row['Harmful Words Count']
        harmful_emoji_count = row['Harmful Emoji Count']
    
        # Process each row's data here
        # print(f"Comment: {comment}, Sentiment: {sentiment_category}, Harmful Words: {harmful_words_count}")

        # Calculate reputation score for this row
        reputation_score = 0
        reputation_score += negative_probability * 60 # Negative probability (out of 60%)
        reputation_score += (
            10 if sentiment_category == "Harmful" else # Sentiment (flag, out of 10%)
            0
        )
        reputation_score += (harmful_words_count/len(comment)) * 20 # Harmful words (out of 20%)
        reputation_score += (
            0 if harmful_emoji_count == 0 else
            3 if harmful_emoji_count == 1 else
            6 if harmful_emoji_count == 2 or harmful_emoji_count == 3 else
            10
        )
        # print(reputation_score)

        # Add or update the user's cumulative reputation score
        if username in user_reputation_scores:
            user_reputation_scores[username] += reputation_score
        else:
            user_reputation_scores[username] = reputation_score

    # Convert to DataFrame for easier viewing if desired
    reputation_df = pd.DataFrame(user_reputation_scores.items(), columns=['Username', 'Cumulative Reputation Score'])
    
    # Sort the DataFrame by 'Cumulative Reputation Score' in descending order
    reputation_df = reputation_df.sort_values(by='Cumulative Reputation Score', ascending=False)

    return reputation_df


########################################################################################################################

# Main Execution

# Comments source file
# json_path = 'comments.json'
json_path = 'output.json'

# Run the harmful comment detection: Analyze comments
analyzed_comments = comments_analysis(json_path)
print(analyzed_comments)

# Get the list accounts who are potentially harassing the given account
reputation_scores_df = get_reputation_score(analyzed_comments)
print(reputation_scores_df)