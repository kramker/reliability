from flask import Flask, request
import os

path1 = os.getcwd() + "\\" + "request"
os.chdir(path1)
app = Flask(__name__)

@app.route('/', methods=["POST"])
def get_math():
    data = request.json
    if len(data) == 3 and type(data['lambda']) == int and type(data['exp']) == int and len(str(data['exp'])) == 1 and '@' in data['email']:
        with open(data['email']+'.txt', "w") as file:
            file.write(str(data)+"\n")
        return "данные получены, ожидайте ответа опеератора"
    else:
        return "Неправильные данные", 400


if __name__ == '__main__':
    app.run("0.0.0.0", 5000)


