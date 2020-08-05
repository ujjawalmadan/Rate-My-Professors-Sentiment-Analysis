import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from predictor import predict_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', comment = 'Sample Comment - Love it here! Definitely made the right choice!')

@app.route('/predict',methods=['POST'])
def predict():
    if request.method == 'POST':
        method = request.form['classifier']
        string = request.form['Comment']
        result, prob = predict_sentiment(string = string, method = method)
        return render_template('index.html', comment = string, prediction_method = 'Method: ' + method, prediction_text= 'Result: ' + str(result[0]), confidence_level = 'Level of Confidence: ' + str(prob))

if __name__ == "__main__":
    app.run(debug=True)