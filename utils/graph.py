import matplotlib
matplotlib.use('Agg')

import io
import base64
import matplotlib.pyplot as plt
from utils.predictor import BASELINE_VALUES

max_values = [1] * 7


def create_graph(data):
    fig, ax = plt.subplots()

    ax.bar(BASELINE_VALUES.keys(), max_values, alpha=0.5, color='green', label='Maximum')
    ax.bar(BASELINE_VALUES.keys(), data, alpha=0.5, color='yellow', label="Relative Values")
    ax.set_title('Comparison between real values and maximum values')
    ax.get_yaxis().set_visible(False)
    plt.xticks(rotation=45)
    ax.legend()

    img = io.BytesIO()
    plt.savefig(img, format='png', bbox_inches='tight')
    plt.close(fig)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode()

    return img_base64

