# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# ======================
# Load & Train Model
# ======================
df = pd.read_csv('NFLX.csv')

X = df[['Open', 'High', 'Low', 'Volume']].values
y = df['Close'].values

x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model_lnr = LinearRegression()
model_lnr.fit(x_train, y_train)

# ======================
# Routes
# ======================
@app.route('/')
def home():
    return "Stock Price Prediction API is running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        open_price = float(data['open'])
        high_price = float(data['high'])
        low_price = float(data['low'])
        volume = float(data['volume'])

        input_data = np.array(
            [open_price, high_price, low_price, volume]
        ).reshape(1, -1)

        prediction = model_lnr.predict(input_data)[0]

        return jsonify({
            "predicted_close": round(float(prediction), 2)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 400


if __name__ == '__main__':
    app.run(debug=True)
