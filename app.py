from flask import Flask, request, jsonify
import sqlite3
import os

app = Flask(__name__)

DATABASE = "noel_service.db"


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()

    conn.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price INTEGER NOT NULL,
            description TEXT,
            image_url TEXT,
            stock INTEGER NOT NULL DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


@app.route("/")
def home():
    return "Noel Service backend is running."


@app.route("/api/products", methods=["GET"])
def get_products():
    conn = get_db()

    products = conn.execute("""
        SELECT *
        FROM products
        ORDER BY id DESC
    """).fetchall()

    conn.close()

    return jsonify([
        dict(product)
        for product in products
    ])


@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No product data supplied"
        }), 400

    name = str(data.get("name", "")).strip()
    category = str(data.get("category", "")).strip()
    description = str(data.get("description", "")).strip()
    image_url = str(data.get("image_url", "")).strip()

    if not name:
        return jsonify({
            "error": "Product name is required"
        }), 400

    if not category:
        return jsonify({
            "error": "Product category is required"
        }), 400

    try:
        price = int(data.get("price", 0))
        stock = int(data.get("stock", 0))
    except (TypeError, ValueError):
        return jsonify({
            "error": "Price and stock must be numbers"
        }), 400

    if price < 0:
        return jsonify({
            "error": "Price cannot be negative"
        }), 400

    if stock < 0:
        return jsonify({
            "error": "Stock cannot be negative"
        }), 400

    conn = get_db()

    cursor = conn.execute("""
        INSERT INTO products
        (name, category, price, description, image_url, stock)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        category,
        price,
        description,
        image_url,
        stock
    ))

    conn.commit()

    product_id = cursor.lastrowid

    conn.close()

    return jsonify({
        "success": True,
        "product_id": product_id
    }), 201


@app.route("/api/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    data = request.get_json()

    if not data:
        return jsonify({
            "error": "No product data supplied"
        }), 400

    conn = get_db()

    existing = conn.execute("""
        SELECT *
        FROM products
        WHERE id = ?
    """, (product_id,)).fetchone()

    if not existing:
        conn.close()

        return jsonify({
            "error": "Product not found"
        }), 404

    name = str(data.get("name", existing["name"])).strip()
    category = str(
        data.get("category", existing["category"])
    ).strip()

    description = str(
        data.get("description", existing["description"] or "")
    ).strip()

    image_url = str(
        data.get("image_url", existing["image_url"] or "")
    ).strip()

    try:
        price = int(data.get("price", existing["price"]))
        stock = int(data.get("stock", existing["stock"]))
    except (TypeError, ValueError):
        conn.close()

        return jsonify({
            "error": "Price and stock must be numbers"
        }), 400

    if price < 0 or stock < 0:
        conn.close()

        return jsonify({
            "error": "Price and stock cannot be negative"
        }), 400

    conn.execute("""
        UPDATE products
        SET
            name = ?,
            category = ?,
            price = ?,
            description = ?,
            image_url = ?,
            stock = ?
        WHERE id = ?
    """, (
        name,
        category,
        price,
        description,
        image_url,
        stock,
        product_id
    ))

    conn.commit()
    conn.close()

    return jsonify({
        "success": True
    })


@app.route("/api/products/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    conn = get_db()

    cursor = conn.execute("""
        DELETE FROM products
        WHERE id = ?
    """, (product_id,))

    conn.commit()

    deleted = cursor.rowcount > 0

    conn.close()

    if not deleted:
        return jsonify({
            "error": "Product not found"
        }), 404

    return jsonify({
        "success": True
    })


init_db()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
