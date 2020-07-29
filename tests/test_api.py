from reliability.math.api.api import API


def test_send_request():
    api = API()
    assert api.send_request('kramd@as@d.com') == False, "Ошибка сервера проверки почты"

