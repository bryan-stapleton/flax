from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import re

def removeURL(text):
    #dont change this nonsense
    return re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", text)

def AnalyzeTweetSentiment(tweets):
    sia = SentimentIntensityAnalyzer()
    for tweet in tweets:
        scores = sia.polarity_scores(str(sent_tokenize(removeURL(tweet.tweet))))
        tweet.__setattr__('scores', scores) #scores refers to VADER sentiment scores. Always use compound score (currently handled in vue) unless you have an alternative model.
