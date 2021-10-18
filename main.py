# Создать класс Main, родительский класс Employee и три произвольных дочерних класса.
# Продемонстрировать наследование полей и метода класса Employee его дочерними классами.
# Сохранить код на гитхаб-аккаунте.

class Main:
    pass


class Employee:
    def __init__(self, q, w, e):
        self.qq = q
        self.ww = w
        self.ee = e

    def ahmat(self):
        print(self.ww)


class Developer(Employee):
    pass


class Doctor(Employee):
    pass


class Gamer(Employee):

    pass


if __name__ == '__main__':
    developer = Developer(12, "Носок", True)
    doctor = Doctor(22, "Джиган", "Олимп")
    gamer = Gamer("Ахмат", "Сила", 95)
    jobs = [gamer, doctor, gamer]
    for j in jobs:
        j.ahmat()
