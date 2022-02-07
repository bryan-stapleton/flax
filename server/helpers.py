import twint, re

def TwintConfig(**kwargs):
    c = twint.Config()
    twint.output.clean_lists()
    old = twint.output.tweets_list
    if (old):
        old.clear()
    if (kwargs['username']):
        c.Username = kwargs['username']
    if (kwargs['search_term']):
        c.Search = kwargs['search_term']
    c.Store_object = True                #creates store data object; required.
    c.Hide_output = True                 #prevents spamming the terminal; required.
    c.Limit = 102                        #recommended to stay at 102 for aesthetics, or below 1000 for speed; required.
    #c.Profile_full = True               #includes shadowbanned accounts & tweets. warning: slow; optional.
    return c

def RemoveDuplicates(tweets):
    seen = set()
    cleaned = []
    for tweet in tweets:
        if tweet.id not in seen:
            cleaned.append(tweet)
            seen.add(tweet.id)
    return cleaned

def SerializeTweets(tweets):
    jt = []
    for tweet in tweets:
        jt.append(vars(tweet))
    return jt

def removeURL(text):
    #dont change this nonsense
    return re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", text)