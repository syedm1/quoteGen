from flask import Flask, jsonify, render_template, request
from flask_restx import Api, Resource
from flask_swagger_ui import get_swaggerui_blueprint
import os
import logging
from QuoteRepository import QuoteRepository

from quotes_dataset import quotes, fall_back_quote

# Configure the logging module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

def main_page():
    return render_template('aboutAPI.html')


def diagnostic():
    return jsonify({'status': 'ok'})

# Define the route for the root path using app.add_url_rule()
app.add_url_rule('/', 'main_page', main_page)
app.add_url_rule('/diagnostic', 'diagnostic', diagnostic)

api = Api(app= app,doc='/docs', version='1.0', title='Quote API', description='API for managing quotes')

quote_repository = QuoteRepository(quotes)

# Swagger UI configuration
SWAGGER_URL = '/api/docs'  # URL for accessing the Swagger UI
API_URL = '/api/swagger.json'  # URL for accessing the API definition JSON file
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Quote API Documentation"
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Define the namespace for the API
ns = api.namespace('api', description='Quote operations')

@ns.route('/random')
class RandomQuoteResource(Resource):
    @api.doc(responses={200: 'OK', 500: 'Internal Server Error'})
    def get(self):
        try:
            return {'quote': quote_repository.get_random_quote()}
        except Exception as e:
            logging.exception(e)
            return {'quote': 'No quote found'}, 500

@ns.route('/quote')
class QuoteResource(Resource):
    @api.doc(responses={200: 'OK', 500: 'Internal Server Error'})
    def get(self):
        try:
            return {'quote': quote_repository.get_random_quote()}
        except Exception as e:
            logging.exception(e)
            return {'quote': 'No quote found'}, 500

@ns.route('/quote/category')
class CategoryQuoteResource(Resource):
    @api.doc(params={'category': 'Category name'}, responses={200: 'OK', 500: 'Internal Server Error'})
    def get(self):
        category = request.args.get('category')
        limit = int(request.args.get('limit', 1))
        try:
            quotes = quote_repository.search_by_category(category, limit=limit)
            return {'quotes': quotes}
        except Exception as e:
            logging.exception(e)
            return {'quote': 'No quotes found for the specified category'}, 500

@ns.route('/quote/author')
class AuthorQuoteResource(Resource):
    @api.doc(params={'author': 'Author name'}, responses={200: 'OK', 500: 'Internal Server Error'})
    def get(self):
        author = request.args.get('author')
        limit = int(request.args.get('limit', 1))
        try:
            quotes = quote_repository.search_by_author(author, limit=limit)
            return {'quotes': quotes}
        except Exception as e:
            logging.exception(e)
            return {'quote': 'No quotes found for the specified author'}, 500

@ns.route('/quote/tag')
class TagQuoteResource(Resource):
    @api.doc(params={'tag': 'Tag name'}, responses={200: 'OK', 500: 'Internal Server Error'})
    def get(self):
        tag = request.args.get('tag')
        limit = int(request.args.get('limit', 1))
        try:
            quotes = quote_repository.search_by_tag(tag, limit=limit)
            return {'quotes': quotes}
        except Exception as e:
            logging.exception(e)
            return {'quote': 'No quotes found for the specified tag'}, 500

@ns.route('/quote/tags')
class TagsQuoteResource(Resource):
    @api.doc(params={'tags': 'Tags (comma-separated)'}, responses={200: 'OK', 500: 'Internal Server Error'})
    def get(self):
        tags = request.args.getlist('tags')
        limit = int(request.args.get('limit', 1))
        try:
            quotes = quote_repository.search_by_tags(tags, limit=limit)
            return {'quotes': quotes}
        except Exception as e:
            logging.exception(e)
            return {'quote': 'No quotes found for the specified tags'}, 500

@app.route('/')
def index():
    return render_template('aboutAPI.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
