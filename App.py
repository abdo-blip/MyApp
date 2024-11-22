from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)




def init_db():
    conn = sqlite3.connect('app.sql')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        quantity INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return "Welcome to The home Page"

@app.route('/add_product', methods=['POST'])
def add_product():
    data = request.json
    name = data.get('name')
    quantity = data.get('quantity')

    if not name or quantity is None:
        return jsonify({'error': 'Invalid data'}), 400

    conn = sqlite3.connect('app.sql')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product added successfully!'}), 201

@app.route('/delete_product/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    conn = sqlite3.connect('app.sql')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product deleted successfully!'}), 200

@app.route('/update_quantity/<int:product_id>', methods=['PUT'])
def update_quantity(product_id):
    data = request.json
    quantity = data.get('quantity')

    if quantity is None:
        return jsonify({'error': 'Invalid data'}), 400

    conn = sqlite3.connect('app.sql')
    cursor = conn.cursor()
    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (quantity, product_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Quantity updated successfully!'}), 200

@app.route('/products', methods=['GET'])
def get_products():
    conn = sqlite3.connect('app.sql')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()

    return jsonify(products), 200

if __name__ == '_main_':
    init_db()
    app.run(debug=True)