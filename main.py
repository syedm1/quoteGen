from flask import Flask, jsonify, render_template
import os
import random
import json
import logging

# Configure the logging module
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = Flask(__name__)

quotes = []

fall_back_quote = {
    "Quote": "Don't cry because it's over, smile because it happened.",
    "Author": "Dr. Seuss",
    "Tags": [
        "attributed-no-source",
        "cry",
        "crying",
        "experience",
        "happiness",
        "joy",
        "life",
        "misattributed-dr-seuss",
        "optimism",
        "sadness",
        "smile",
        "smiling "
    ],
    "Popularity": 0.15566615566615566,
    "Category": "life"
}


def load_quotes():
    with open('public/quotes.json', 'r', encoding='utf-8') as file:
        quotes.extend(json.load(file))


def get_quote():
    try:
        quote = random.choice(quotes)
        return jsonify({'quote': quote})
    except Exception as e:
        logging.exception(e)
        return jsonify({'quote': fall_back_quote})


@app.route('/diagnostic', methods=['GET'])
def diagnostic():
    return jsonify({'status': 'ok'})


@app.route('/api/quote', methods=['GET'])
def send_quote():
    try:
        return get_quote()
    except:
        return jsonify({'quote': 'No quote found'}), 500


@app.route('/')
def index():
    return render_template('aboutAPI.html')


if __name__ == '__main__':
    logger.info("Can access dataset: " + str(os.path.exists('quotes.json')))
    load_quotes()
    app.run(debug=True, port=os.getenv("PORT", default=5000))
