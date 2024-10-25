from flask import Flask, render_template, jsonify
import requests
import os

app = Flask(__name__)

# API للحصول على نكت عشوائية
@app.route('/api/joke', methods=['GET'])
def get_joke():
    response = requests.get('https://official-joke-api.appspot.com/jokes/random')
    if response.status_code == 200:
        joke_data = response.json()
        return jsonify({'setup': joke_data['setup'], 'punchline': joke_data['punchline']})
    return jsonify({'error': 'Unable to fetch joke'}), 500

# واجهة المستخدم (الرئيسية)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    # الحصول على المنفذ من المتغيرات البيئية
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
