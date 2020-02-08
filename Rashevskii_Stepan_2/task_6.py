# catalog = [
#    (1, {'название': 'компьютер', 'цена': int(input('Введите стоимость: ')),
#         'количество': int(input('Введите количество: ')), 'eд': 'шт.'}),
#    (2, {'название': 'принтер', 'цена': int(input('Введите стоимость: ')),
#         'количество': int(input('Введите количество: ')), 'eд': 'шт.'}),
#    (3, {'название': 'сканер', 'цена': int(input('Введите стоимость: ')),
#         'количество': int(input('Введите количество: ')), 'eд': 'шт.'})
# ]

catalog = [
    (1, {'название': 'компьютер', 'цена': 20000, 'количество': 5, 'eд': 'шт.'}),
    (2, {'название': 'принтер', 'цена': 6000, 'количество': 2, 'eд': 'шт.'}),
    (3, {'название': 'сканер', 'цена': 2000, 'количество': 7, 'eд': 'шт.'})
]

keys_of_catalog = list(catalog[0][1].keys())
value = catalog[0][1]['название']
result = {
    keys_of_catalog[0]: [catalog[0][1]['название'], catalog[1][1]['название'], catalog[2][1]['название']],
    keys_of_catalog[1]: [catalog[0][1]['цена'], catalog[1][1]['цена'], catalog[2][1]['цена']],
    keys_of_catalog[2]: [catalog[0][1]['количество'], catalog[1][1]['количество'], catalog[2][1]['количество']],
    keys_of_catalog[3]: [catalog[0][1]['eд'], catalog[1][1]['eд'], catalog[2][1]['eд']],
}

result_2 = {}
items = []

for keys in keys_of_catalog:
    for item in catalog:
        items.append(item[1][keys])
    result_2[keys] = items
    items = []
print(result)
print(result_2)
