import csv
import json
import sqlite3

from flask import Flask, render_template, request

def create_database():
    """Creates and populates the SQLite database."""
    conn = sqlite3.connect("products.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """
    )
    cursor.execute(
        """
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES
        (1, 'Laptop', 'Electronics', 799.99),
        (2, 'Coffee Mug', 'Home Goods', 15.99)
    """
    )
    conn.commit()
    conn.close()


def read_json_products():
    """Reads product data from a JSON file."""
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def read_csv_products():
    """Reads product data from a CSV file."""
    products = []
    try:
        with open("products.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                try:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                    products.append(row)
                except (ValueError, KeyError):
                    continue
        return products
    except (FileNotFoundError, csv.Error):
        return None

def read_sql_products(product_id=None):
    """
    Reads product data from the SQLite database, with optional filtering by id.
    """
    products = []
    try:
        conn = sqlite3.connect("products.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if product_id:
            cursor.execute("SELECT * FROM Products WHERE id=?", (product_id,))
        else:
            cursor.execute("SELECT * FROM Products")

        products = [dict(row) for row in cursor.fetchall()]
        conn.close()
        return products
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        return None


app = Flask(__name__)


@app.route("/products")
def products_list():
    """
    Displays products from JSON, CSV, or SQL based on the 'source' query parameter.
    Filters by 'id' if provided.
    """
    source = request.args.get("source")
    product_id = request.args.get("id")

    data = None
    error = None

    if source == "json" or source == "csv":
        if source == "json":
            data = read_json_products()
        else:
            data = read_csv_products()

        if data and product_id:
            try:
                product_id = int(product_id)
                data = [p for p in data if p["id"] == product_id]
                if not data:
                    error = "Product not found."
            except ValueError:
                error = "Invalid product ID. ID must be an integer."
                data = None

    elif source == "sql":

        try:
            if product_id:
                product_id = int(product_id)
            data = read_sql_products(product_id)
            if not data:
                error = "Product not found."
        except ValueError:
            error = "Invalid product ID. ID must be an integer."
            data = None

    else:
        error = "Wrong source. Please specify 'json', 'csv', or 'sql'."

    if data is None and error is None:
        error = "Could not load data from the specified source."

    return render_template("product_display.html", products=data, error=error)


if __name__ == "__main__":
    create_database()
    app.run(debug=True, port=5000)
