from flask import Blueprint, request, render_template
import os

# from utils.graph import create_graph

# from utils.predictor import Predictor, BASELINE_VALUES
# import pandas as pd
# import torch

models = Blueprint(
    "models", __name__, template_folder="templates", static_folder="static"
)
# predictor = Predictor()

import requests


@models.route("/", methods=["GET", "POST"], strict_slashes=False)
def index():
    if request.method == "GET":
        return render_template("models/index.html")
    elif request.method == "POST":
        keys = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
        input_dict = {}
        for key in keys:
            if key not in request.form.keys():
                return "Missing key in form data"
            else:
                input_dict[key] = float(request.form.get(key))


        try:
            response = requests.post(str(os.environ.get("API_URL", "https://nkca122-fasalguru.hf.space/predict")), json=input_dict)

            response.raise_for_status()
            data = response.json()

            return render_template(
                "models/result.html",
                result=data["prediction"],
                confidence=data["confidence"] * 100,
                values=list(input_dict.items()),
            )
        except requests.exceptions.RequestException as e:
            return f"Something went wrong: {str(e)}"

    else:
        return "Invalid method"
