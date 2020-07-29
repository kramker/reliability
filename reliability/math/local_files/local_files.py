import os
import datetime

from reliability.math.api.Math_main import Math
from reliability.math.api.api import API

path = os.getcwd() + "\\" + "user"
os.chdir(path)
api = API()
math = Math()

class LocalFiles:
    email = ""
    def new_use(self, email):
        if api.send_request(email) == True:
            if os.path.exists(os.getcwd() + "\\" + email+".txt") == False:
                with open(email+'.txt', 'w') as f:
                    f.write(str(datetime.date.today())+"\n")
                print("Пользователь успешно создан")
                LocalFiles.email = email
                return True
            else:
                print("Пользователь уже существует")
                return False

    def load_use(self, email):
        if os.path.exists(os.getcwd() + "\\" + email+".txt") == True:
            LocalFiles.email = email
            print("Авторизация прошла успешно")
            return True
        else:
            print("Пользователь не найден")
            return False

    def active_use(self, operation, x="1"):
        email = LocalFiles.email
        with open(email+'.txt', 'a') as f:
            str1 = math.time(operation, x)
            str1 = str(str1)
            if x == "1":
                g = "эксплутации"
            else:
                g = "хранении"
            f.write("При лямбда равной " + operation + " срок надежности при " + g + " равен " + str1 + " часов\n")






