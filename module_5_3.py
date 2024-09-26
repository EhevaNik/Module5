class House:

    def __init__(self, name, number_of_floors):
        self.name = name  # имя
        self.number_of_floors = number_of_floors  # количество этажей

#__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
    def __len__(self):
        return self.number_of_floors

# __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".
    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

# должны присутствовать в классе и возвращать результаты сравнения по соответствующим операторам
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

# увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self

    def __radd__(self, value):
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
            return self



# исходные данные
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
