import sys

from reliability.math.api.Math_main import Math
from reliability.math.api.api import API
from reliability.math.local_files.local_files import LocalFiles

k = "2"
create = []
suc_login = 0
mat = Math()
api = API()
loc = LocalFiles()
for param in sys.argv:
    create.append(param)
print("ввёдён параметр: " + create[1])

if create[1] == "new":
    email = input("Введите почту:\n")
    if loc.new_use(email) == True:
        e = email
        k = email
        suc_login = 1
elif create[1] == "login":
    email = input("Введите почту:\n")
    if loc.load_use(email) == True:
        e = email
        k = email
        suc_login = 1
else:
    print("ошибка авторизации")


while k != "2":
    if suc_login == 1:
        lambd = input("Введите лямбду:\n")
        x = input("Введите 1 для эксплутации или 2 для хранения:\n")
        print(mat.time(lambd, x))
        loc.active_use(lambd, x)
        k = input("Введите 1 для нового запроса или 2 для конца работы:\n")
        if k != "1" and k != "2":
            print("Неверное значение")
            sys.exit()
    else:
        k = "2"
print("Конец работы")
sys.exit()
