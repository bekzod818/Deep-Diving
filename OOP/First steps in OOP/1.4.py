class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")


media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()


class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        print(
            *[
                item
                for item in self.data
                if item in range(self.LIMIT_Y[0], self.LIMIT_Y[1] + 1)
            ]
        )


graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()


class Stepik:
    def next_task(self):
        return "Следующее задание"


my_st = Stepik()

import sys


class StreamData:
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for index, key in enumerate(fields):
                setattr(self, key, lst_values[index])
            return True
        return False


class StreamReader:
    FIELDS = ("id", "title", "pages")

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()

import sys

# программу не менять, только добавить два метода
lst_in = list(
    map(str.strip, sys.stdin.readlines())
)  # считывание списка строк из входного потока


class DataBase:
    lst_data = []
    FIELDS = ("id", "name", "old", "salary")

    def insert(self, data: list):
        for item in data:
            self.lst_data.append(dict(zip(self.FIELDS, item.split())))

    def select(self, a, b):
        l = len(self.lst_data)
        if b >= l:
            return self.lst_data[a:]
        return self.lst_data[a : b + 1]


db = DataBase()
db.insert(lst_in)


class Translator:
    def add(self, eng, rus):
        if "tr" not in self.__dict__:
            self.tr = {}

        self.tr.setdefault(eng, [])
        # здесь продолжайте метод add
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)

    def remove(self, eng):
        # здесь продолжайте метод remove
        if eng in self.tr:
            del self.tr[eng]

    def translate(self, eng):
        # здесь продолжайте метод translate
        return self.tr.get(eng, [])


# здесь создавайте объект класса Translator
tr = Translator()
tr.add("tree", "дерево")
tr.add("car", "машина")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove("car")
print(" ".join(tr.translate("go")))
