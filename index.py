from flask import Flask, request, jsonify

app = Flask(__name__)

# ===== Model Weights (من التدريب) =====
COEFFICIENTS = [0.52, 0.31, -0.12, 0.000001]
INTERCEPT = 3.47

@app.route('/')
def home():
    return "Stock Prediction API Running"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        open_p = float(data['open'])
        high_p = float(data['high'])
        low_p = float(data['low'])
        volume = float(data['volume'])

        prediction = (
            COEFFICIENTS[0] * open_p +
            COEFFICIENTS[1] * high_p +
            COEFFICIENTS[2] * low_p +
            COEFFICIENTS[3] * volume +
            INTERCEPT
        )

        return jsonify({
            "predicted_close": round(prediction, 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == '__main__':
    app.run()
