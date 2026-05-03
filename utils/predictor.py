import torch
import torch.nn as nn
import pickle

HIDDEN_NEURONS = 10
BASELINE_VALUES = {
    "N": 140,
    "P": 145,
    "K": 205,
    "temperature": 43.67549305,
    "humidity": 99.98187601,
    "ph": 9.93509073,
    "rainfall": 298.5601175
}


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.input_layer = nn.Linear(7, HIDDEN_NEURONS)
        self.hidden_layer = nn.Linear(HIDDEN_NEURONS, HIDDEN_NEURONS)
        self.output = nn.Linear(HIDDEN_NEURONS, 22)

        self.relu = nn.ReLU()  # ReLU for hidden layers
        self.softmax = nn.Softmax(dim=1)  # Softmax for multi-class classification

    def forward(self, x):
        x = self.relu(self.input_layer(x))
        x = self.relu(self.hidden_layer(x))
        x = self.output(x)
        x = self.softmax(x)

        return x


class Predictor:
    Tabular = Model()

    def __init__(self):
        Predictor.Tabular.load_state_dict(torch.load("./predictors/tabular_sowing_classification.pt"))

    def predict_class(self, prediction):
        with open("./predictors/label_encoder.pkl", "rb") as f:
            label_encoder = pickle.load(f)
        return label_encoder.inverse_transform([prediction])[0]
