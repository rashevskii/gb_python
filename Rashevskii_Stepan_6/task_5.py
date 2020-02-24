class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def __init__(self, title):
        super(Pen, self).__init__(title)

    def draw(self):
        print('Запуск отрисовки ручкой')


class Pencil(Stationery):
    def __init__(self, title):
        super(Pencil, self).__init__(title)

    def draw(self):
        print('Запуск отрисовки карандашем')


class Handle(Stationery):
    def __init__(self, title):
        super(Handle, self).__init__(title)

    def draw(self):
        print('Запуск отрисовки маркером')


pen = Pen('Ручка')
pen.draw()
print(pen.title)

pencil = Pencil('Карандаш')
pencil.draw()
print(pencil.title)

handle = Handle('Маркер')
handle.draw()
print(handle.title)
