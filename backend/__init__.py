from flask import Flask, request, jsonify
from backend.data import sales_per_month, sales_per_seller, best_selling_products
from backend.config import app, cors

# Apagar home page
@app.route("/", methods=["GET", "POST"])
def home_page():
    return jsonify({"message": "API funcionando"}), 200

# show the graphs selected by the user.
@app.route("/api/sales/<graph_type>", methods=["POST"])
def get_sales(graph_type):

    # receive what the user selected.
    data = request.get_json()
    if not data:
        return(
            jsonify({"message": "JSON inválido"}), 400
        )
    years = data.get("years")
    months = data.get("months")

    # error message if user does not select any month or year.
    if not years or not months:
        return(
            jsonify({"message": "Você deve selecionar pelo menos um mês e um ano."}), 400
        )

    # take the processed data and send it using JSON
    if graph_type == "monthly":
        result = sales_per_month(years, months)
    
    elif graph_type == "seller":
        result = sales_per_seller(years, months)
        print(result)

    elif graph_type == "product":
        result = best_selling_products(years, months)

    # show the selected graphics by the user.
    return jsonify(result), 200
