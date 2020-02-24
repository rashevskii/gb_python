class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super(Position, self).__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f'{self.name} {self.surname}')

    def get_total_income(self):
        print(f'{self._income["wage"] + self._income["bonus"]}')


pos = Position('Ivan', 'Ivanov', 'money maker', 50000, 150000)
pos.get_full_name()
pos.get_total_income()
