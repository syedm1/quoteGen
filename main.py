from flask import Flask, jsonify, render_template
import os
import random
import json

app = Flask(__name__)

quotes = []


def load_quotes():
    with open('quotes.json', 'r', encoding='utf-8') as file:
        quotes.extend(json.load(file))


@app.route('/diagnostic', methods=['GET'])
def diagnostic():
    return jsonify({'status': 'ok'})


@app.route('/api/quote', methods=['GET'])
def get_quote():
    quote = random.choice(quotes)
    return jsonify({'quote': quote})


@app.route('/')
def index():
    return render_template('aboutAPI.html')


if __name__ == '__main__':
    load_quotes()
    app.run(debug=True, port=os.getenv("PORT", default=5000))
