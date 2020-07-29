import sys
class Math:
    def time(self,lambd,x):
        if x == "1":
            return 1/(int(lambd)*10 ** (-6))
        elif x == "2":
            return 1/(int(lambd)*10 ** (-8))
        else:
            return "Неверное значение"

