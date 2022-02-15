#local imports
from helpers import TwintConfig, PerformSearch
from database.db import db, AddToDatabase, QueryTweets

#external imports
from flask import Flask, jsonify
from flask_cors import CORS
from flask_restx import Api, Resource

# note: needs to be the twint branch with user agent fix
## FLASK SETUP ##
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/bryan/Documents/flax/server/database/temp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
api = Api(app)

## ROUTES ##
#TODO: Landing page for data visualizer + GUI to interact with api directly. Currently handled by swagger auto generated docs. Docs need updating.
@app.route('/')
def landing():
    return

@api.route('/advanced/<username>/')
@api.route('/advanced/<username>/<search_term>')
class AdvancedSearch(Resource):
    def get(self, username, search_term=None):
        c = TwintConfig(username=username, search_term=search_term)
        res = PerformSearch(c)
        AddToDatabase(res)
        QueryTweets()
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
    app.run(debug=True, threaded=True)