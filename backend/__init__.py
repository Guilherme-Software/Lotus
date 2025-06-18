from flask import Flask, request, jsonify
from backend.data import sales_per_month, sales_per_seller, best_selling_products
from backend.config import app, cors


@app.route("/", methods=["GET", "POST"])
def home_page():
    if request.method == "POST":
        graphic = request.files.get("graphic")
        if not graphic:
            return(
                jsonify({"message": "Arquivo inválido."}), 400
            )
        else:
            return(
                jsonify({"message": "Arquivo recebido!"}), 200
            )
        
    return jsonify({"message": "API funcionando"}), 200


@app.route("/api/sales/<graphic_type>", methods=["POST"])
def get_sales(graphic_type):
    data = request.get_json()
    print("JSON recebido:", data)
    if not data:
        return(
            jsonify({"message": "JSON inválido"}), 400
        )
    years = data.get("years")
    months = data.get("months")

    if not years or not months:
        return(
            jsonify({"message": "Você deve selecionar pelo menos um mês e um ano."}), 400
        )

    if graphic_type == "monthly":
        result = sales_per_month(years, months)
    
    elif graphic_type == "seller":
        result = sales_per_seller(years, months)

    elif graphic_type == "product":
        result = best_selling_products(years, months)

    else:
        return(
            jsonify({"message": "Selecione o tipo do gráfico."}), 400
        )
    
    return jsonify(result), 200
