#local imports
from helpers import db, TwintConfig, PerformSearch, AddToDatabase, QueryTweets

#external imports
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
from flask_restx import Api, Resource
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import close_all_sessions
import os

## FLASK SETUP ##
app = Flask(__name__, static_folder='dist', static_url_path='/')

uri = os.getenv("DATABASE_URL",  'sqlite:///database/tmp.db')  #fixes heroku postgres dialect bug
if uri and uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
api = Api(app)
ma = Marshmallow(app)

def init_db():
    app.app_context().push() # This is only needed on initial setup.
    with app.app_context():  # Builds database tables and connects app to db.
        db.init_app(app)
        close_all_sessions() 
        db.drop_all()         
        db.create_all()      

## ROUTES ##
#TODO: Landing page for data visualizer + GUI to interact with api directly. Currently handled by swagger auto generated docs. Docs need updating.
@api.route('/app')
class LandingPage(Resource):
    def get(self):
        return send_from_directory('dist', 'index.html')

@api.route('/db/query/')
class DatabaseQuery(Resource):
    def get(self):
        res = QueryTweets()
        return jsonify(res) 

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

init_db() #only needed on initial startup

if __name__ == "__main__":
    app.run(port=os.environ.get('PORT', 5000))
    