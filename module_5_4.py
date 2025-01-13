class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls) # cls.houses_history

    def __init__(self, name_floor, number_of_floors):
        self.name_floor = str(name_floor)
        self.number_of_floors = int(number_of_floors)

    def __del__(self):
        print(f"{self.name_floor} снесён, но он останется в истории")

dom1 = House('ЖК Горский', 10)
print(House.houses_history)
dom2 = House('ЖК Акация', 20)
print(House.houses_history)
dom3 = House('ЖК Матрёшки', 30)
del dom2
del dom3
print(House.houses_history)

