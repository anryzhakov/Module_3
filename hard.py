# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Дополнительное практическое задание по модулю: "Подробнее о функциях."

def calculate_structure_sum(*args):
    sum = 0
    for items in args:
        if isinstance(items, int):
            sum += items
        elif isinstance(items, float):
            sum += items
        elif isinstance(items, bool):
            sum += items
        elif isinstance(items, str):
            sum += len(items)
        elif isinstance(items, list):
            sum += calculate_structure_sum(*items)
        elif isinstance(items, tuple):
            sum += calculate_structure_sum(*items)
        elif isinstance(items, set):
            sum += calculate_structure_sum(*items)
        elif isinstance(items, dict):
            sum += calculate_structure_sum(*tuple(items.items()))
    return sum


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print('Результат: ', result)