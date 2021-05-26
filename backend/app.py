from urllib.parse import parse_qs, urlparse

import requests
from flask import Flask, jsonify
from flask_restful import Api, Resource

from scraper import Scraper

app = Flask(__name__)
api = Api(app)


class TakeABreak(Resource):
    def get(self):
        scraper = Scraper()
        return scraper.pick_random()


class Recommendations(Resource):
    def get(self, title):
        scraper = Scraper()
        return jsonify(scraper.get_movie_id_by_title(title))

    def put(self, name, category):
        pass


class HelloWorld(Resource):
    def get(self, name):
        return jsonify({'name': name})


api.add_resource(TakeABreak, '/')
api.add_resource(Recommendations, '/<string:title>')
# api.add_resource(HelloWorld, '/<string:name>')

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='localhost')
