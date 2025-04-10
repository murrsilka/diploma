# Алёна Шевелько, 28-когорта - Финальный проект. Инженер по тестированию плюс

import requests
import configuration

# Создаем заказ, отправляя POST-запрос на указанный URL-адрес.
def create_order(order_data):
    response = requests.post(f"{configuration.URL_SERVICE}/{configuration.ORDERS_URL}", json=order_data)
    return response.json()

# Получаем информацию о заказе по его трек-номеру, отправляя GET-запрос на указанный URL-адрес.
def get_order_by_track(track):
    response = requests.get(f"{configuration.URL_SERVICE}/{configuration.TRACK_URL}{track}")
    return response.status_code