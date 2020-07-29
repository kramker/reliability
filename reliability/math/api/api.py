import requests

from reliability.math.api.const import BASE_URL



class API:
    def send_request(self, texts):
        email = BASE_URL+texts
        response = requests.post(email).json()
        if response["format_valid"] == True:
            print("Проверка формата почты: успешно")
            return True
        elif response["format_valid"] == False:
            print("Проверка формата почты: неверный формат почты")
            return False
        else:
            print("Ошибка работы API")
            return False