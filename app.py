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

# Sample orders data
orders = []

@app.route('/orders')
def get_orders():
    return jsonify(orders)

@app.route('/place_order', methods=['POST'])
def place_order():
    orders.append({"order_id": len(orders) + 1, "product_id": 1})
    return jsonify({"message": "Order placed successfully"})



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003)