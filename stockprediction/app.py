from flask import Flask, render_template, request, jsonify
import yfinance as yf
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

model = LinearRegression()

def train_model():
    stock_data = yf.download('AAPL', start='2022-01-01', end='2023-01-01')
    X = stock_data[['Open', 'High', 'Low', 'Volume']].values
    y = stock_data['Close'].values
    model.fit(X, y)

train_model()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    stock_symbol = data.get('symbol')
    stock_data = yf.download(stock_symbol, start='2022-01-01', end='2023-01-01')
    X_new = stock_data[['Open', 'High', 'Low', 'Volume']].values
    prediction = model.predict(X_new)[-1] + 100
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
