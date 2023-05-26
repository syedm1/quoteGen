from flask import Flask, jsonify, render_template
import os
import random
import logging
from quotes_dataset import quotes, fall_back_quote
# Configure the logging module
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger(__name__)

app = Flask(__name__)

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
    app.run(debug=True, port=os.getenv("PORT", default=5000))
