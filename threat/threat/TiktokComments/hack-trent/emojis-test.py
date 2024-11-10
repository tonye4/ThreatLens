  

#to detect a threat detection level based on certain words and phrases and if the user follows you
import nltk
import time #to check for runtime
import re
import codecs #to read unicode from a file

from nltk.corpus import stopwords
from nltk.tokenize.regexp import regexp_tokenize #using regexp to quickly search through text
#from nltk.stem import WordNetLemmatizer
from multiprocessing import Pool  #using pool to create faster lemmatization (https://stackoverflow.com/questions/38019823/faster-lemmatization-techniques-in-python)


#########################################################
#        #cleaning texts with emoji. Removing any       #
#        #unwanted emojis and just keeping the emojis   #
#        #that may be considered harassments/           #
#        #threats                                       #
#########################################################


#opening text file of emoji unicode
def load_emojis(path):
    with codecs.open(path, "r", encoding="utf-8") as file:
        emojis = file.read().strip().split()  # Splitting to treat each emoji as an individual entry
    return emojis # returns the emojis as a list of strings

def emojis_analysis(text, path="potentially_harmful_emojis.txt"):
    harmful_emojis = set(load_emojis(path))  # Use a set for quicker lookup
    harmful_emoji_count = 0
    for char in text:
        if char in harmful_emojis:
            harmful_emoji_count += 1
            print(f"Found harmful emoji: {char}")  # Debugging line to confirm matching emojis
        else:
            print(f"Non-harmful or unrecognized emoji: {char}")  # For tracking mismatches
    return harmful_emoji_count


# Main Execution
path = "potentially_harmful_emojis.txt"

count = emojis_analysis("💣YOU ARE 💣💣")
print(count)

###########################################################
#                                                         #
#             Tokenize (splitting phrases into words)     #
#             and also using stopwords (removing          #
#               unnecessary words) to clean up the        #
#               texts                                     #
#                                                         #        
###########################################################

#references: https://www.datacamp.com/tutorial/text-analytics-beginners-nltk

# #using core to allow cpu to handle multple task simulationously
# def processingText(text, cores = 4):

#     text_emojis = text_with_emojis(text)


#     #creating a regex to include special characters (including asterick, exclamation points, dollar sign), and emoji to detect harassment (https://www.w3schools.com/python/python_regex.asp)
#     pattern = r'[a-zA-Z\*\!\$]+' + "|"  + "|".join(harassment_emojis)
#     tokens = regexp_tokenize(text_emojis.lower(), pattern) #making strings to be lowercase for sentimental analysis

#     #removes stopwords from text (https://stackoverflow.com/questions/19560498/faster-way-to-remove-stop-words-in-python/68677841)
#     stop_words = set(stopwords.words("english"))
#     filter_tokens = [token for token in tokens if token not in stop_words]

#     #using lemmatization from nltk so it links words that are similar to each other, or root words together (with similar meaning)
#     #lemmatizer = WordNetLemmatizer()
#     #with Pool(processes=cores) as pool:
#         #lemmatizer_tokens = pool.map(lemmatizer.lemmatize, filter_tokens)
    
#     #making sure to join the texts back into a string
#     processing_Text = ' '.join(filter_tokens)
#     processing_Text = re.sub(r'\s+', ' ', processing_Text) #this is to rejoin the text without the extra spaces
#     return processing_Text
 