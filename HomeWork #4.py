# Слушатель курса Junior Python-разработчик
# Рыжаков Андрей Николаевич, anryzhakov@yandex.ru
# Самостоятельная работа по уроку "Произвольное число параметров".

def single_root_words(root_word, *other_words):
    same_words = list()
    rw = root_word.upper()
    for i in other_words:
        ow = i.upper()
        sw1 = ow.find(rw); sw2 = rw.find(ow)
        if sw1 != -1 or sw2 != -1:
            same_words.append(i)
    return same_words

res1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
res2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(res1)
print(res2)