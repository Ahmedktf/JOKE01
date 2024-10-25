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

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
