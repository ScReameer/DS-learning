from flask import Flask, request, jsonify
import datetime as dt
import numpy as np
import pickle

app = Flask(__name__)

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
    # Передаём один объект с 4 признаками
    features = request.json
    features = np.array(features).reshape(1, 4)
    # Десериализация модели
    with open(r'F:\SF-DS-practice\Block-7\DS_PROD-1\model.pkl', 'rb') as model_pkl:
        model = pickle.load(model_pkl)
    # Получение предсказания для объекта
    prediction = model.predict(features)[0]
    # Возвращаем в виде json
    return jsonify({'prediction': prediction})
    
if __name__ == '__main__':
    app.run('localhost', 5000)