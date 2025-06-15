from flask import Flask
from flask import jsonify
from main.data import sales_per_month, sales_per_seller, best_selling_products
from main.config import app


@app.route("/api/sales")
def get_sales():
    sales = sales_per_month(2025)
    return jsonify(sales)

@app.route("/api/sellers")
def get_sellers():
    sellers = sales_per_seller(2025)
    return jsonify(sellers)

@app.route("/api/products")
def get_products():
    products = best_selling_products(2024)
    return jsonify(products)

app