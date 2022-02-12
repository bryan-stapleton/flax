from helpers import TwintConfig, PerformSearch

from flask import Flask
from flask_cors import CORS
from flask_restx import Api, Resource
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

# note: needs to be the twint branch with user agent fix
## FLASK SETUP ##
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/bryan/Documents/flax/server/database/temp.db'
CORS(app)
api = Api(app)
db = SQLAlchemy(app)
ma = Marshmallow(app)

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
        return PerformSearch(c)

@api.route('/search/<search_term>')
class Search(Resource):
    def get(self, search_term):
        c = TwintConfig(username=None, search_term=search_term)
        return PerformSearch(c)

#TODO: fix location-based search route
#@api.route('/location/<location>')
#class LocationSearch(Resource):
    #def get(self, location):
    #    c = TwintConfig(username=None, search_term=None, geo=location)
    #    twint.run.Search(c)
    #    t = twint.output.tweets_list[:c.Limit]
    #    AnalyzeTweetSentiment(t)
    #    j = ReturnTweetsJson(t)
    #    return j

## APP ##
if __name__ == "__main__":
    app.run(debug=True, threaded=True)