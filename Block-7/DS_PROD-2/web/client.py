import requests

if __name__ == '__main__':
    # выполняем POST-запрос на сервер по эндпоинту prediction с параметром json
    r = requests.post('http://localhost:5000/predict', json={'features': [1, 2, 3, 4]})
    # выводим статус запроса
    print(r.status_code)
    # реализуем обработку результата
    if r.status_code == 200:
        # если запрос выполнен успешно (код обработки=200),
        # выводим результат на экран
        print(r.json()['prediction'])
    else:
        # если запрос завершён с кодом, отличным от 200,
        # выводим содержимое ответа
        print(r.text)
