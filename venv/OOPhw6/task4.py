# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.

class Car:

    def __init__(self, name, speed, color, is_police, direction):
        self.direction = direction
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(is_police)

    def show_speed(self):
        return f'\nСкорость= {self.speed}'

    def go(self):
        if self.speed != 0:
            print('Машина поехала')

    def stop(self):
        if self.speed == 0:
            print('Машина остановилась')

    def turn(self, direction):
        if self.direction == 'left':
            print('Машина поворачивает налево')
        if self.direction == 'right':
            print('Машина поворачивает направо')



