class House:
    def __init__(self, name, number_of_floors):
        self.name = str(name)
        self.number_of_floors = int(number_of_floors)


    def go_to(self, new_floor):
        self.new_floor = int(new_floor)
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует!")
        else:
            for i in range(1,self.new_floor + 1):
                print("| %2.0f |" % int(i))

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
       return str(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))
