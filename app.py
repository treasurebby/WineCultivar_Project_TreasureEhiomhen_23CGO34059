# app.py
from flask import Flask, render_template, request
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model & scaler
model_path = os.path.join("model", "wine_cultivar_model.joblib")
scaler_path = os.path.join("model", "scaler.joblib")

model = joblib.load(model_path)
scaler = joblib.load(scaler_path)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    probabilities = None

    if request.method == "POST":
        try:
            # Get 6 values from form
            flavanoids    = float(request.form["flavanoids"])
            od280         = float(request.form["od280"])
            color_int     = float(request.form["color_intensity"])
            proline       = float(request.form["proline"])
            alcohol       = float(request.form["alcohol"])
            hue           = float(request.form["hue"])

            # Create array in correct order
            features = np.array([[
                flavanoids,
                od280,
                color_int,
                proline,
                alcohol,
                hue
            ]])

            # Scale
            features_scaled = scaler.transform(features)

            # Predict
            pred = model.predict(features_scaled)[0]
            prob = model.predict_proba(features_scaled)[0]

            cultivar_map = {0: "Cultivar 0", 1: "Cultivar 1", 2: "Cultivar 2"}
            prediction = cultivar_map[pred]

            probabilities = {
                "Cultivar 0": round(prob[0]*100, 1),
                "Cultivar 1": round(prob[1]*100, 1),
                "Cultivar 2": round(prob[2]*100, 1)
            }

        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html",
                          prediction=prediction,
                          probabilities=probabilities)


if __name__ == "__main__":
    app.run(debug=True)