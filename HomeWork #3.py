# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашнее задание по уроку "Распаковка позиционных параметров".

# 1.
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
    return

print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# 2.
values_list = [23.4, 'Note', (3, 7, 55)]
values_dict = {'a': 'Book', 'b': 33.6, 'c': 777}

print_params(*values_list)
print_params(**values_dict)

# 3.
values_list_ = [53.4, 'NoteBook']

print_params(*values_list_, 42)