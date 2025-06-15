from flask import Flask, request, jsonify
from main.data import sales_per_month, sales_per_seller, best_selling_products
from main.config import app


@app.route("/api/sales/monthly", methods=["GET", "POST"])
def get_sales():
    if request.method == "GET":
        years = request.args
    sales = sales_per_month([2024, 2025], [5, 7, 8])
    return jsonify(sales)

@app.route("/api/sales/seller")
def get_sellers():
    sellers = sales_per_seller(2025)
    return jsonify(sellers)

@app.route("/api/sales/product")
def get_products():
    products = best_selling_products(2024, 2025)
    return jsonify(products)

app