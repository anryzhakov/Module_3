# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Самостоятельная работа по уроку "Рекурсия"

def get_multiplied_digits(number):

    str_number = str(number)
    first = int(str_number[0])
    print(str_number, first, len(str_number[1:]))
    if len(str_number[1:]) >= 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

number = int(input('Введите любое целое число, не оканчивающееся нулем: '))
result = get_multiplied_digits(number)
print ('Итого: ', result)