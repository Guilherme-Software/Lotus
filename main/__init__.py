from flask import Flask
from flask import jsonify
from main import sales_per_month

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        month = sales_per_month()
        return jsonify({
            "mensage":"Hello"
        })
    
    return app


