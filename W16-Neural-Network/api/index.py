from flask import Flask, request, jsonify
from flask_cors import CORS
from neural_network import load_full
import numpy as np

app = Flask(__name__)
CORS(app, origins=["https://daynel-kem.github.io"])

model = load_full("shape_predictor.npy")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    shape_input = data.get("shape")
    print(shape_input)
    x = np.array(shape_input).reshape(1, 100)
    pred = model.predict(x)

    if pred[0, 0] > pred[0, 1] and pred[0, 0] > pred[0, 2]:
        return jsonify({
            "prediction": "Rectangle",
            "Confidence": pred.tolist(),
        })
    elif pred[0, 1] > pred[0, 0] and pred[0, 1] > pred[0, 2]:
        return jsonify({
            "prediction": "Circle",
            "Confidence": pred.tolist(),
        })
    else:
        return jsonify({
            "prediction": "Triangle",
            "Confidence": pred.tolist(),
        })

if __name__ == "__main__":
    app.run(debug=True)