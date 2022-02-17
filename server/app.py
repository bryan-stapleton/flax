#local imports
from helpers import TwintConfig, PerformSearch
from database.models import db, Tweet, TweetSchema

#external imports
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource
from flask_marshmallow import Marshmallow
#from sqlalchemy.orm import close_all_sessions #uncomment this import for initial database setup

## FLASK SETUP ##
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/bryan/Documents/flax/server/database/temp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
api = Api(app)
ma = Marshmallow(app)

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
    schema = TweetSchema()
    #for n in db.session.query(Tweet).filter_by(username='joebiden').order_by(Tweet.datetime):
    return schema.dump(Tweet.all())

## ROUTES ##
#TODO: Landing page for data visualizer + GUI to interact with api directly. Currently handled by swagger auto generated docs. Docs need updating.
@app.route('/')
def landing():
    return

@app.route('/private/query/')
class DatabaseQuery(Resource):
    def post(self):
        res = "placeholder"
        return jsonify(res)
    
    def get(self):
        t = QueryTweets()
        return t

@api.route('/advanced/<username>/')
@api.route('/advanced/<username>/<search_term>')
class AdvancedSearch(Resource):
    def get(self, username, search_term=None):
        c = TwintConfig(username=username, search_term=search_term)
        res = PerformSearch(c)
        AddToDatabase(res)
        return jsonify(res)

@api.route('/search/<search_term>')
class Search(Resource):
    def get(self, search_term):
        c = TwintConfig(username=None, search_term=search_term)
        res = PerformSearch(c)
        AddToDatabase(res)
        return jsonify(res)

## APP ##
if __name__ == "__main__":
    db.init_app(app)
    #app.app_context().push() #This is only needed on initial setup.
    #with app.app_context(): #Builds database tables and connects app to db.
    #    close_all_sessions() #Will need to uncomment the close_all_sessions import above.
    #    db.drop_all()
    #    db.create_all()
    app.run(debug=True, threaded=True)
    