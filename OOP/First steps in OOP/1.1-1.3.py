class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Point(2, 3)
p2 = Point(4, 5)

print(p1.x, p1.y)
print(p2.x, p2.y)


class DataBase:
    pk: int = 1
    title: str = "Классы и объекты"
    author: str = "Сергей Балакирев"
    views: int = 14356
    comments: int = 12


# Любители однострочников
Database = type(
    "Database",
    (),
    {
        "pk": 1,
        "title": "Классы и объекты",
        "author": "Сергей Балакирев",
        "views": 14356,
        "comments": 12,
    },
)


class Figure:
    type_fig: str = "ellipse"
    color: str = "red"


fig1 = Figure()
setattr(Figure, "start_pt", (10, 5))
setattr(Figure, "end_pt", (100, 20))
setattr(Figure, "color", "blue")

del Figure.color

print(*fig1.__dict__.keys())
