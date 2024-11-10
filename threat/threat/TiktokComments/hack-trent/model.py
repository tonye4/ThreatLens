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

# Function that loads json data
def load_data(json_path):
    # Open the JSON file in read mode
    with open(json_path, 'r') as file:
        # Load the JSON data into a Python dictionary or list (depending on JSON structure)
        data = json.load(file)
    # Convert the loaded JSON data to a pandas DataFrame for easier manipulation
    return pd.DataFrame(data)

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
    print(score)
    neg_score = score['neg']
    # Determine sentiment category
    sentiment_category = "Harmful" if score['neg'] > (score['pos'] + score['neu'])/2 else "Non-Harmful"
    return neg_score, sentiment_category

# # Function that defines the sentiment category (harmful or non-harmful)    
# def sentiment_category(score):
#     if score['neg'] > (score['pos'] + score['neu'])/2:
#         return "Harmful"
#     else:
#         return "Non-Harmful"
    
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
    harmful_emoji_count = 0
    
    for emoji in hamrful_emojis:
        print(text)
        print('\n\n')
        if emoji in text:
            harmful_emoji_count += 1 
    
    # for char in text:
    #     print(char)
    #     print('\n')
    #     if char in harmful_emojis:
    #         harmful_emoji_count += 1
    #         print(f"Found harmful emoji: {char}")  # Debugging line to confirm matching emojis
    #         print(f"Non-harmful or unrecognized emoji: {char}")  # For tracking mismatches
    return harmful_emoji_count

    # harmful_emojis = load_emojis(path)  # List of harmful emojis
    # harmful_emoji_count = 0

    # # Extract emojis from the text using emoji library
    # text_emojis = emoji.emoji_list(text)

    # # Debugging: Print out the emojis found in the text
    # print(f"Extracted emojis: {[emj['emoji'] for emj in text_emojis]}")

    # # Check if any of the extracted emojis are in the harmful emojis list
    # for emj in text_emojis:
    #     extracted_emoji = emj['emoji']
    #     if extracted_emoji in harmful_emojis:
    #         harmful_emoji_count += 1
    #         print(f"Found harmful emoji: {extracted_emoji}")  # Debugging: Show which harmful emoji is found

    # return harmful_emoji_count



# Wrapper Function to Identify harmful comments    
# Function to detect harmful comments
def detect_harmful_comments(json_path):
    # load the data from the json file
    comments = load_data(json_path)
    # sentiment analysis: How likely it is for the comment to be negative, sentiment category (based on negative score)
    comments[['Negative Probability', 'Sentiment Category']] = comments['comment'].apply(lambda text: pd.Series(sentiment_analysis(text)))
    # keyword matching: count number of offensive words in a comment
    comments['Harmful Words Count'] = comments['comment'].apply(keywords_analysis)
    comments['Harmful Emoji Count'] = comments['comment'].apply(emojis_analysis)     
    return comments



# Reputation score: assigned to users based on their past behavior (e.g., number of harmful comments flagged over time).
# COMPLETE!!!!
# Modify to take more things into consideration
def get_reputation_score(analyzed_comments):
    # neg_probability = analyzed_comments['Negative Probability']
    # sentiment = analyzed_comments['Sentiment Category']
    harmful_count = analyzed_comments[analyzed_comments['Sentiment Category'] == 'Harmful'].groupby('username').size()
    return harmful_count

########################################################################################################################

# Main Execution
json_path = 'comments.json'
# Run the harmful comment detection
analyzed_comments = detect_harmful_comments(json_path)
print(analyzed_comments)

reputation_scores = get_reputation_score(analyzed_comments)
# Create a DataFrame of the highest harassers (users with the most harmful comments)
highest_harassers = reputation_scores.reset_index()
highest_harassers.columns = ['User Account', 'Harmful Score']

print(highest_harassers)