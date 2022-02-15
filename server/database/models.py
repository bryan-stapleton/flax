from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#The attributes that are commented out can be added back in by uncommenting them below in the class definition and the init function. 
#The attributes will need to be set in the AddToDatabase function as well. AddToDatabase can be found in db.py.
#For the sake of simplicity I am not adding them to the database as of now as they're not useful to me. Feel free to add or remove attributes as desired.

#Several attributes, notably including 'mentions' and 'near', are not properly configured and will cause errors if simply uncommented. 
#After investigation this appears to be because they are returning arrays and/or dictionaries instead of strings. 
#Will need to either create another db model and a relationship, or dissect the dictionaries and add the keys as attributes.

class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    datetime = db.Column(db.String(64))
    user_id = db.Column(db.String(64))
    username = db.Column(db.String(64))
    tweet = db.Column(db.String(280))
    lang = db.Column(db.String(64))
    scores = db.Column(db.Integer)
    #id_str = db.Column(db.String(64))
    #conversation_id = db.Column(db.String(64))
    #datestamp = db.Column(db.String(64))
    #timestamp = db.Column(db.String(64))
    #user_id_str = db.Column(db.String(64))
    #name = db.Column(db.String(64))
    #place = db.Column(db.String(64))
    #mentions = db.Column(db.String(256))
    #reply_to = db.Column(db.String(64))
    #urls = db.Column(db.String(64))
    #photos = db.Column(db.String(64))
    #video = db.Column(db.String(64))
    #thumbnail = db.Column(db.String(64))
    #hashtags = db.Column(db.String(64))
    #likes_count = db.Column(db.String(64))
    #link = db.Column(db.String(128))
    #retweet = db.Column(db.String(64))
    #retweet_id = db.Column(db.String(64))
    #retweet_date = db.Column(db.String(64))
    #user_rt = db.Column(db.String(64))
    #user_rt_id = db.Column(db.String(64))
    #near = db.Column(db.String(128))
    #source = db.Column(db.String(64))
    #translate = db.Column(db.String(64))
    #trans_src = db.Column(db.String(64)) 
    
    def __init__(self, id, datetime, user_id, username, tweet, lang, score):
        self.id = id
        self.datetime = datetime
        self.user_id = user_id
        self.username = username
        self.tweet = tweet
        self.lang = lang
        self.score = score
        #self.id_str = id_str
        #self.conversation_id = conversation_id
        #self.datestamp = datestamp
        #self.timestamp = timestamp
        #self.user_id_str = user_id_str
        #self.name = name
        #self.place = place
        #self.mentions = mentions
        #self.reply_to = reply_to
        #self.urls = urls
        #self.photos = photos
        #self.video = video
        #self.thumbnail = thumbnail
        #self.hashtags = hashtags
        #self.likes_count = likes_count
        #self.link = link
        #self.retweet = retweet
        #self.retweet_id = retweet_id
        #self.retweet_date = retweet_date
        #self.user_rt = user_rt
        #self.user_rt_id = user_rt_id
        #self.quote_url = quote_url
        #self.near = near
        #self.geo = geo
        #self.source = source
        #self.translate = translate
        #self.trans_src = trans_src
    
    def __repr__(self):
        return f'[{self.id}: {self.tweet} -@{self.username} posted:{self.datetime}]'