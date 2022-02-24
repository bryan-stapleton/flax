#local imports
from helpers import db, TwintConfig, PerformSearch, AddToDatabase, QueryTweets
#external imports
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource
from flask_marshmallow import Marshmallow
from sqlalchemy.orm import close_all_sessions

## FLASK SETUP ##
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database/tmp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
api = Api(app)
ma = Marshmallow(app)

def init_db():
    app.app_context().push() # This is only needed on initial setup.
    with app.app_context():  # Builds database tables and connects app to db.
        close_all_sessions() 
        db.drop_all()         
        db.create_all()      

## ROUTES ##
#TODO: Landing page for data visualizer + GUI to interact with api directly. Currently handled by swagger auto generated docs. Docs need updating.
@app.route('/')
def landing():
    return

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
if __name__ == "__main__":
    db.init_app(app)
    #init_db() #only needed on initial startup
    app.run(debug=True, threaded=True)
    