from server import db

## DB ##
class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_str = db.Column(db.String(32))
    conversation_id = db.Column(db.String(32))
    datetime = db.Column(db.String(32))
    datestamp = db.Column(db.String(64))
    timestamp = db.Column(db.String(64))
    user_id = db.Column(db.String(32))
    user_id_str = db.Column(db.String(32))
    username = db.Column(db.String(32))
    name = db.Column(db.String(32))
    place = db.Column(db.String(32))
    mentions = db.Column(db.String(32))
    reply_to = db.Column(db.String(32))
    urls = db.Column(db.String(64))
    photos = db.Column(db.String(64))
    video = db.Column(db.String(64))
    thumbnail = db.Column(db.String(64))
    tweet = db.Column(db.String(1000))
    lang = db.Column(db.String(32))
    hashtags = db.Column(db.String(64))
    likes_count = db.Column(db.String(32))
    link = db.Column(db.String(128))
    retweet = db.Column(db.String(32))
    retweet_id = db.Column(db.String(32))
    retweet_date = db.Column(db.String(64))
    user_rt = db.Column(db.String(32))
    user_rt_id = db.Column(db.String(32))
    near = db.Column(db.String(128))
    source = db.Column(db.String(32))
    translate = db.Column(db.String(32))
    trans_src = db.Column(db.String(32))
    scores = db.Column(db.String(128))


    def __init__(self, id, id_str, conversation_id, datetime, datestamp, timestamp, user_id, user_id_str, username, name, place, mentions, reply_to, urls, photos, video, thumbnail, tweet, 
    lang, hashtags, likes_count, link, retweet, retweet_id, retweet_date, user_rt, user_rt_id, quote_url, near, geo, source, translate, trans_src, scores):
        self.id = id
        self.id_str = id_str
        self.conversation_id = conversation_id
        self.datetime = datetime
        self.datestamp = datestamp
        self.timestamp = timestamp
        self.user_id = user_id
        self.user_id_str = user_id_str
        self.username = username
        self.name = name
        self.place = place
        self.mentions = mentions
        self.reply_to = reply_to
        self.urls = urls
        self.photos = photos
        self.video = video
        self.thumbnail = thumbnail
        self.tweet = tweet
        self.lang = lang
        self.hashtags = hashtags
        self.likes_count = likes_count
        self.link = link
        self.retweet = retweet
        self.retweet_id = retweet_id
        self.retweet_date = retweet_date
        self.user_rt = user_rt
        self.user_rt_id = user_rt_id
        self.quote_url = quote_url
        self.near = near
        self.geo = geo
        self.source = source
        self.translate = translate
        self.trans_src = trans_src
        self.scores = scores
    
    def __repr__(self):
        return f'[{self.id}, {self.id_str}]'