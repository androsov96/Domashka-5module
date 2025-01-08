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

dom1 = House('ЖК Горский', 18)
dom2 = House('Домик в деревне', 2)
dom1.go_to(5)
dom2.go_to(10)