from flask import Flask, request, jsonify
import datetime as dt
import numpy as np
import pickle

app = Flask(__name__)

# Десериализация модели
with open(r'F:\SF-DS-practice\Block-7\DS_PROD-2\web\models\model.pkl', 'rb') as model_pkl:
    model = pickle.load(model_pkl)

# GET
@app.route('/hello')
def hello_func():
    name = request.args['name']
    return f'hello!, {name}'

@app.route('/')
def index():
    return 'Test message. The server is running'

@app.route('/time')
def current_time():
    return str(dt.datetime.now())

# POST
@app.route('/add', methods=['POST'])
def add():
    num = request.json['num']
    if num > 10:
        return 'too much', 400
    return jsonify({'result': num + 1})

@app.route('/predict', methods=['POST'])
def predict():
    features = np.array(request.json['features'])
    features = features.reshape(1, 4)
    prediction = model.predict(features)
    return  jsonify({'prediction': prediction[0]})
    
if __name__ == '__main__':
    app.run('localhost', 5000)