<<<<<<< HEAD
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Endpoint لجلب أسعار العملات الرقمية
@app.route('/api/prices', methods=['GET'])
def get_prices():
    currency_id = request.args.get('id', 'bitcoin')  # افتراضيًا: بيتكوين
    try:
        response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={currency_id}&vs_currencies=usd")
        data = response.json()

        # التحقق من وجود العملة
        if currency_id not in data:
            return jsonify(error="Currency not found"), 404

        return jsonify(data)
    except Exception as e:
        return jsonify(error=str(e)), 500

=======
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
>>>>>>> 1c0f9abb45de69cf541ec1dd878f321eef65eca7
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(debug=True)
=======
    # الحصول على المنفذ من المتغيرات البيئية
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
>>>>>>> 1c0f9abb45de69cf541ec1dd878f321eef65eca7
