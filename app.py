from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

with open('greenbook_data.json') as f:
    data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.json['query'].lower()
    results = [entry for entry in data if query in json.dumps(entry).lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)