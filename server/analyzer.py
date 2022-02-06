from helpers import removeURL
from nltk.tokenize import sent_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer

def AnalyzeTweetSentiment(tweets):
    sia = SentimentIntensityAnalyzer()
    for tweet in tweets:
        scores = sia.polarity_scores(str(sent_tokenize(removeURL(tweet.tweet))))
        tweet.__setattr__('scores', scores) #scores refers to VADER sentiment scores. Always use compound score (currently handled in vue) unless you have an alternative model.
