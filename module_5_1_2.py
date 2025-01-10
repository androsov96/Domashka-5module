class House:
    def __init__(self, name_floor, number_of_floors):
        self.name_floor = str(name_floor)
        self.number_of_floors = int(number_of_floors)

    def __len__(self):
        return self.number_of_floors
    def __str__(self):
        return f'Название: {self.name_floor}, кол-во этажей: {self.number_of_floors}'
    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __add__(self, value):
        self.number_of_floors += value
        return self.number_of_floors
    def __radd__(self, value):
        return self.__add__(value)
    def __iadd__(self, value):
        return self.__add__(value)

dom1 = House('ЖК Горский', 10)
dom2 = House('ЖК Акация', 20)

print(dom1)
print(dom2)
print(dom1 == dom2) # __ed__
dom1.__add__(10) # __add__
print(dom1)
print(dom1 == dom2)
dom1.__iadd__(10)   # __iadd__
print(dom1)
dom2.__radd__(10) # __radd__
print(dom2)
print(dom1 > dom2) # __gt__
print(dom1 >= dom2) # __ge__
print(dom1 > dom2) # __lt__
print(dom1 <= dom2) # __le__
print(dom1 != dom2) # __ne__


