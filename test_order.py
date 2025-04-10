# Алёна Шевелько, 28-когорта - Финальный проект. Инженер по тестированию плюс

from stand import create_order, get_order_by_track
from data import order_data

def test_get_order_by_track():
    # Создаем заказ и получаем трекинговый номер
    order = create_order(order_data)
    track = order["track"]

    # Проверяем, что трекинговый номер не является пустым
    assert track is not None

    # Получаем статус код и JSON-ответ при запросе информации о заказе по трекинговому номеру
    status_code = get_order_by_track(track)

    # Проверяем, что статус код равен 200 (успешный запрос)
    assert status_code == 200