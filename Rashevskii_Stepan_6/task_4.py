class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction):
        print(f'Машина повернула {direction}')

    def show_speed(self):
        print(f'Скорость машины {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


    def show_speed(self):
        if self.speed > 60:
            print('Превышение скорости!')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Превышение скорости!')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


town_car = TownCar(65, 'red', 'Volvo', False)
sport_car = SportCar(120, 'red', 'Honda', False)
work_car = WorkCar(50, 'blue', 'Isuzu', False)
police_car = PoliceCar(90, 'black', 'Audi', True)
town_car.go()
sport_car.stop()
work_car.turn('направо')
police_car.show_speed()
town_car.show_speed()
work_car.show_speed()
print(town_car.color)
