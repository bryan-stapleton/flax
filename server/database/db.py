from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from database.models import Tweet

db = SQLAlchemy()
ma = Marshmallow()

def AddToDatabase(tweets):
    for tweet in tweets:
        exists = Tweet.query.filter_by(id=tweet['id']).first()
        if exists:
            print('tweet already exists')
            continue
        else:
            tweet_to_add = Tweet(id=tweet['id'], datetime=tweet['datetime'], lang=tweet['lang'], user_id=tweet['user_id'], username=tweet['username'], tweet=tweet['tweet'], score=tweet['scores']['compound'])
            try:
                db.session.add(tweet_to_add)
                print('tweet added to db')
            except Exception as e:
                print(e)
                continue
    db.session.commit()
    print('tweets committed to db')

def QueryTweets():
    #for n in db.session.query(Tweet).filter_by(username='joebiden').order_by(Tweet.datetime):
    for n in db.session.query(Tweet).all():
        print(n)