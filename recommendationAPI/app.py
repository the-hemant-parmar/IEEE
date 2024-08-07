from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from update_handler import update_rating, top_n_products


app = Flask(__name__)
# to start the server
## first activate the virtual environment
## then 'python -m flask run [filename if not app.py]'


@app.route(
    "/<n_prod>", methods=["GET"]
)  # just want to get the default top ranking items
def top_recommendations(n_prod: str = 5):
    if n_prod.isnumeric():
        if n_prod:
            n_prod = int(n_prod)
        else:
            n_prod = 5
        recommendations = list(top_n_products(n_prod))
        # print(recommendations)
        recommendations = [f"amazon.in/dp/{prod_asin}" for prod_asin in recommendations]
        return jsonify(recommendations)
    else:
        return "Inappropriate request"


@app.route(
    "/update/", methods=["POST"]
)  # insert the given producct and update the top ranking items accordingly
def update_recommendations():
    url = request.form.get("url")
    # print(url)
    if request.method == "POST" and url:
        # the url should be from amazon and look like http://amazon.com/dp/[product_asin]/foo
        idx = url.find("/dp/")
        prod_asin = url[idx + 4 :].split("/")[0]
        print(prod_asin)
        if idx >= len(url):
            return "wrong url format!", 400
        else:
            update_rating(prod_asin)
            return "Success!", 200
    else:
        return "bad request!", 400
