import time


class TrafficLight:

    def running(self):
        _color = 'Красный'
        moment = time.time()
        while time.time() - moment < 7:
            print(_color)
        _color = 'Желтый'
        moment = time.time()
        while time.time() - moment < 2:
            print(_color)
        _color = 'Зеленый'
        moment = time.time()
        while time.time() - moment < 7:
            print(_color)


t_l = TrafficLight()
t_l.running()
