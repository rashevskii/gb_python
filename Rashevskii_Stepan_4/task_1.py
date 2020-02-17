from sys import argv


def get_wage(hours, costs, bonus):
    return (hours * costs) + bonus


if len(argv) == 4:
    hours = int(argv[1])
    costs = int(argv[2])
    bonus = int(argv[3])
    print(get_wage(hours=int(argv[1]), costs=int(argv[2]), bonus=int(argv[3])))
elif len(argv) == 3:
    hours = int(argv[1])
    costs = int(argv[2])
    print(get_wage(hours=int(argv[1]), costs=int(argv[2]), bonus=0))


