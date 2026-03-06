from flask import Flask, render_template, request
from src.predict import predict_transaction

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    features = [float(x) for x in request.form.values()]

    result = predict_transaction(features)

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)
    