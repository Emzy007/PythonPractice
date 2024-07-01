from flask import Flask, jsonify, request
import requests
import random
import string

app = Flask(__name__)

def generate_share():
    return {
        'symbol': ''.join(random.choices(string.ascii_uppercase + string.digits, k=5)),
        'price': round(random.uniform(10.5, 200.5), 2),
        'value_date': random.randint(20220101, 20221231)
    }

@app.route('/get_shares', methods=['GET'])
def get_shares():
    num = request.args.get('num', default = 1, type = int)
    shares = [generate_share() for _ in range(num)]
    return jsonify(shares)

if __name__ == '__main__':
    app.run(debug=True)