class House:

    def __init__(self, name, number_of_floors):
        self.name = name  # имя
        self.number_of_floors = number_of_floors  # количество этажей

# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно), на который нужно приехать.
    def go_to(self, new_floor):
        floor = 1
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for floor in range(new_floor):
                print(floor+1)

# исходные данные
h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)