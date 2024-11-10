**Problem Statement**

Online threats and harassment are on the rise
Harassment can take many forms: bullying, hate speech, sexual harassment, and harmful behavior.

TikTok, with its massive user base, faces unique challenges in monitoring and moderating harmful content at scale.
Difficulties in identifying harmful content in real-time due to the sheer volume of posts and the complexity of language (e.g., slang, emojis).
Increased risks to user mental health → vulnerable users, including teens and marginalized groups.

**Run Instructions for the code**

Fork the repository. Then run this command in your directory

```pip install -r requirements.txt```

Then run this command after navigating to ```ThreatLens/backend```
And run this command: 

```python manage.py runserver```



**Technology and Tools Used**

**Core Technologies:**
Python: Used as the main programming language for its versatility and extensive libraries.
Pandas: Essential for data manipulation and analysis, especially in structuring and filtering comments.
NLTK: Natural Language Toolkit used for language processing, including SentimentIntensityAnalyzer for sentiment analysis.
Backend and Frontend Frameworks:
Django (Backend): Handles server-side operations, stores analyzed results, and enables communication with the frontend.
React (Frontend): Used to display flagged comments and harmful user scores in an intuitive, user-friendly way, offering real-time updates on detected threats.

**Core Functionality**

Sentiment Analysis: Uses NLP to assess the emotional tone of comments, flagging high negativity or aggression.
Emotional tone of text
Detects if the comment is harmful or non-harmful
Returns the probability of the comment being negative
Keyword Detection: Matches against a list of known harmful words to identify abusive language.
Keyword matching
Checks the amount of times keywords from an offensive speech list appear in comments
Emoji Analysis: Tracks emojis commonly associated with harmful or harassing intent.
Identifies potentially harmful emojis in the comment
Keeps a count of the harmful emojis in comments

**Key Components**

Data Scraper: 
Collects data from social media platforms by utilizing APIs and web scraping techniques.
Gathers user comments and posts, creating a rich dataset for analyzing online interactions and flagging harmful content.
Data Processing and Analysis: 
Employs Natural Language Processing (NLP) to evaluate the sentiment and tone of each comment, detecting signs of potentially threatening or aggressive language.
Uses sentiment analysis to score the likelihood of harmful intent, flagging comments with high negativity or aggression.

**Importance of Detecting Harmful Content**

Early detection helps prevent harm by flagging inappropriate content before it escalates.
Protects users' well-being by identifying and addressing harmful language.
Streamlines content moderation, making it easier to spot and address harmful posts.
Supports platform safety policies and enforces community guidelines for safer online spaces.
Ensures accountability by tracking and addressing harassment.
Promotes healthier online environments by reducing toxicity.

**Project Goals:**

Detect harmful content in comments by analyzing sentiment, keywords, and emojis.
Target harmful behaviors such as hate speech, harassment, and bullying to promote safer online spaces.

**CHALLENGE: FORENSIC SCIENCE**

Digital Forensics Contribution: Identifies and flags harmful content, like hate speech and harassment, on platforms like TikTok for investigation.
Digital Evidence Gathering: Analyzes comments, emojis, and sentiment to identify digital “clues” of harassment or abuse, akin to forensic evidence collection.
Accuracy in Detection: Uses multiple methods—sentiment analysis, harmful keyword detection, and emoji analysis—for accurate and automated detection, ensuring consistent results.
Real-World Impact: Addresses the rise in online harassment and threats, providing timely interventions and supporting investigations into digital criminal activities like cyberbullying. 
