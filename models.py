from flask import Blueprint, request, render_template

from utils.graph import create_graph
from utils.predictor import Predictor, BASELINE_VALUES
import pandas as pd
import torch

models = Blueprint('models', __name__, template_folder='templates', static_folder='static')
predictor = Predictor()


@models.route('/', methods=['GET', 'POST'], strict_slashes=False)
def index():
    if request.method == 'GET':
        return render_template('/models/index.html')
    elif request.method == 'POST':
        keys = ["N", "P", "K", "temperature", "humidity", "ph", "rainfall"]
        input_dict = {}
        for key in keys:
            if key not in request.form.keys():
                return "Missing key in form data"
            else:
                input_dict[key] = float(request.form.get(key)) / BASELINE_VALUES[key]

        input_tensor = torch.tensor([list(input_dict.values())], dtype=torch.float32)
        df = pd.DataFrame.from_dict({key: [float(val * BASELINE_VALUES[key])] for key, val in input_dict.items()})
        # Graph
        img_base64 = create_graph(input_dict.values())
        with torch.no_grad():
            prediction = predictor.Tabular(input_tensor)
        predicted_class_num = prediction.argmax(dim=1).item()
        result = predictor.predict_class(predicted_class_num)

        return render_template("/models/result.html", result=result.upper(), graph=img_base64,
                               values=[round(val, 1) for val in df.values[0].tolist()],
                               columns=[col.upper() for col in df.columns.tolist()])
    else:
        return "Invalid method"
