from flask import Flask, jsonify, render_template, request
import os
import logging
from QuoteRepository import QuoteRepository

from quotes_dataset import quotes, fall_back_quote

# Configure the logging module
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

quote_repository = QuoteRepository(quotes)


@app.route('/diagnostic', methods=['GET'])
def diagnostic():
    return jsonify({'status': 'ok'})


@app.route('/api/random', methods=['GET'])
def get_random_quote():
    try:
        return jsonify({'quote': quote_repository.get_random_quote()})
    except Exception as e:
        logging.exception(e)
        return jsonify({'quote': 'No quote found'}), 500


@app.route('/api/quote', methods=['GET'])
def get_quote():
    try:
        return jsonify({'quote': quote_repository.get_random_quote()})
    except Exception as e:
        logging.exception(e)
        return jsonify({'quote': 'No quote found'}), 500


@app.route('/api/quote/category', methods=['GET'])
def search_by_category():
    category = request.args.get('category')
    limit = int(request.args.get('limit', 1))
    try:
        quotes = quote_repository.search_by_category(category, limit=limit)
        return jsonify({'quotes': quotes})
    except Exception as e:
        logging.exception(e)
        return jsonify({'quote': 'No quotes found for the specified category'}), 500


@app.route('/api/quote/author', methods=['GET'])
def search_by_author():
    author = request.args.get('author')
    limit = int(request.args.get('limit', 1))
    try:
        quotes = quote_repository.search_by_author(author, limit=limit)
        return jsonify({'quotes': quotes})
    except Exception as e:
        logging.exception(e)
        return jsonify({'quote': 'No quotes found for the specified author'}), 500


@app.route('/api/quote/tag', methods=['GET'])
def search_by_tag():
    tag = request.args.get('tag')
    limit = int(request.args.get('limit', 1))
    try:
        quotes = quote_repository.search_by_tag(tag, limit=limit)
        return jsonify({'quotes': quotes})
    except Exception as e:
        logging.exception(e)
        return jsonify({'quote': 'No quotes found for the specified tag'}), 500


@app.route('/api/quote/tags', methods=['GET'])
def search_by_tags():
    tags = request.args.getlist('tags')
    limit = int(request.args.get('limit', 1))
    try:
        quotes = quote_repository.search_by_tags(tags, limit=limit)
        return jsonify({'quotes': quotes})
    except Exception as e:
        logging.exception(e)
        return jsonify({'quote': 'No quotes found for the specified tags'}), 500


@app.route('/')
def index():
    return render_template('aboutAPI.html')


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
