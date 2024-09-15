# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашняя работа по уроку "Пространство имён"

calls = 0

def count_calls(): # Функция №1. Подсчет количества вызовов функций
    global calls
    calls += 1
    return (calls)

def string_info(string): # Функция №2. Возвращает кортеж по условиям п.2
    string_list = list()
    string_list.append(len(string))
    string_list.append(string.upper())
    string_list.append(string.lower())
    count_calls()
    print(string_list)
    return()

def is_contains(string, list_to_search): # Функция №3. Возвращает jndtn по условиям п.3
    flag = False
    str = string.upper()
    for i in list_to_search:
        if str == i.upper():
            flag = True
    print(flag)
    count_calls()
    return()

string_info('Capybara')
string_info('Armageddon')
is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)
