from flask import Flask, request, jsonify
import requests

# 🔹 لازم الاسم يكون app
app = Flask(__name__)

BACKEND_URL = "https://youssefalamgad9.pythonanywhere.com/predict"

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "ok",
        "service": "vercel proxy"
    })

@app.route("/predict", methods=["GET", "POST"])
def predict():
    try:
        if request.method == "POST":
            data = request.get_json(force=True)
            r = requests.post(BACKEND_URL, json=data, timeout=10)
        else:
            r = requests.get(BACKEND_URL, params=request.args, timeout=10)

        return jsonify(r.json()), r.status_code

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


