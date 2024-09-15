# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Домашняя работа по уроку "Способы вызова функции"

def send_email (message, recipient,
               sender = "university.help@gmail.com"):

    tld_re = -1; tld_se = -1
    tld_list = (".com", ".ru", ".net")

# 1.Проверка на корректность e-mail отправителя и получателя.
    for i in tld_list:
        tld_re = recipient.find(i)
        if tld_re != -1:
            break
    for i in tld_list:
        tld_se = sender.find(i)
        if tld_se != -1:
            break
    if tld_re == -1 or '@' not in recipient:
        print (f'Невозможно отправить письмо на адрес {recipient}')
        return
    if tld_se == -1 or '@' not in recipient:
        print (f'Невозможно отправить письмо с адреса {sender}')
        return

# 2.Проверка на отправку самому себе.
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return

# 3.Если отправитель совпадает  с  отправителем по умолчанию -
# university.help@gmail.com
    if sender == 'university.help@gmail.com':
        print(f"Письмо успешно отправлено с адреса {sender} "
              f"на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено "
              f"с адреса {sender} на адрес {recipient}.")
        return

send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

# Следующие символы запрещено использовать в адресе
# электронной почты (RFC 2822):
#   пробел и табуляция
#   знак восклицания (!)
#   решётка (#)
#   знак доллара ($)
#   процент (%)
#   амперсанд (&)
#   тильда (~)
#   знак равно (=)
#   запятая (,)
#   апостроф (')
#   более одной точки подряд