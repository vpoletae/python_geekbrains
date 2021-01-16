#1
# a little bit unclear with the task so a little bit poor realization
from time import sleep

class TrafficLight(object):

    __color = ['red', 'yellow', 'green']
    __time_lags = [7, 2, 2]
    __colors_len = len(__color)

    def running(self):
        for i in range(TrafficLight.__colors_len):
            print(f'Current traffic light is {TrafficLight.__color[i]}')
            sleep(TrafficLight.__time_lags[i])

tr_light_1 = TrafficLight()
tr_light_1.running()

#2
class Road(object):
    _consumption = 25
    _density = 5

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def count_mass(self):
        return self._length * self._width * Road._consumption * Road._density

road1 = Road(100, 50)
new_mass = road1.count_mass()
print(new_mass)

#3
class Worker(object):
    
    def __init__(self, name, surname, position, wage, bonus):
        self._name = name
        self._surname = surname
        self._position = position
        self._income = {'wage': wage, 'bonus': bonus}

class Position(Worker):
    
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return f'{self._name} {self._surname}'

    def get_total_income(self):
        wage = self._income['wage']
        bonus = self._income['bonus']
        return wage + bonus

worker1 = Position('Ivan', 'Ivanov', 'accountant', 20000, 5000)
print(worker1.get_full_name())
print(worker1.get_total_income())

#4
class Car(object):
    
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('The car goes!')

    def stop(self):
        print('The car has stopped!')

    def turn(self, direction):
        print(f'The car has turned to the {direction}')

    def show_speed(self):
        print(f'Current speed is {self.speed} km//h')


class TownCar(Car):
    
    def __init(self, speed, color, name, is_police):
        super().__init__()

    def show_speed(self):
        if self.speed > 60:
            print('Caution! Speed limit was exceeded. Please slow down!')
        else:
            print(f'Current speed is {self.speed} km//h')


class SportCar(Car):

    def __init(self, speed, color, name, is_police):
        super().__init__()


class WorkCar(Car):

    def __init(self, speed, color, name, is_police):
        super().__init__()

    def show_speed(self):
        if self.speed > 40:
            print('Caution! Speed limit was exceeded. Please slow down!')
        else:
            print(f'Current speed is {self.speed} km//h')


class PoliceCar(Car):

    def __init(self, speed, color, name, is_police):
        super().__init__()

sport_car = SportCar(100, 'yellow', 'ferrari', 0)
town_car = TownCar(65, 'gray', 'renault', 0)
work_car = WorkCar(40, 'white', 'kamaz', 0)
police_car = PoliceCar(80, 'black-white', 'citroen', 80)

sport_car.go()
sport_car.stop()
sport_car.turn('right')
sport_car.show_speed()
print('-'*40)
print('Town car attributes')
print(town_car.speed)
print(town_car.name)
print(town_car.color)
print(town_car.is_police)
town_car.show_speed()
print('-'*40)
print(police_car.is_police)
print('-'*40)
work_car.show_speed()

#5
class Stationary(object):

    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Draw initialize')


class Pen(Stationary):

    def __init__(self, title='Pen'):
        super().__init__(title='Pen')

    def draw(self):
        print('Drawing with a pen')


class Pencil(Stationary):

    def __init__(self, title='Pencil'):
        super().__init__(title='Pencil')

    def draw(self):
        print('Drawing with a pencil')


class Handle(Stationary):

    def __init__(self, title='Handle'):
        super().__init__(title='Handle')

    def draw(self):
        print('Drawing with a handle')


pen = Pen()
print(pen.title)
pen.draw()
print('-'*40)
pencil = Pencil()
print(pencil.title)
pencil.draw()
print('-'*40)
handle = Handle()
print(handle.title)
handle.draw()