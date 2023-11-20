from flask import Flask, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {"id": 1, "name": "Product A", "price": 10.0},
    {"id": 2, "name": "Product B", "price": 15.0},
]

@app.route('/products')
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)