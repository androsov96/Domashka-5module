class House:
    def __init__(self, name_floor, number_of_floors):
        self.name_floor = str(name_floor)
        self.number_of_floors = int(number_of_floors)


    def go_to(self, new_floor):
        for i in range(1, new_floor + 1 ):
            if new_floor > self.number_of_floors or new_floor < 1:
                print('Такого этажа не существует')
                break
            else:
                print(i)

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name_floor}, кол-во этажей: {self.number_of_floors}'

dom1 = House('ЖК Горский', 18)
dom2 = House('Домик в деревне', 2)
print(dom1)
print(dom2)
print(len(dom1))
print(len(dom2))
