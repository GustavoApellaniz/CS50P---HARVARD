class Vehicle:

    def __init__(self, name = 'f', max_speed = 4, mileage = 0):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
    
    def __str__(self):
        return f'{self.name} , {self.max_speed}, {self.mileage}'

    def fds(self):
        print('hernaça nessa nidj iohbqij   ONLBK   ')
    



class minicar(Vehicle):
    def __init__(self, name = 0, max_speed = 0, mileage = 0):
        super().__init__(name, max_speed, mileage)




car = minicar('quero que se foda')

print(car)
car.fds()