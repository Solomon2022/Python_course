# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен
# записываться в новый текстовый файл.

from translate import Translator

translator = Translator(from_lang='en', to_lang='ru')

line_list = []
with open('text_4.txt', 'r', encoding='utf-8') as f_r:
    with open('new_text_4', 'a', encoding='utf-8') as f_a:
        for el in f_r:
            line_list = el.split()
            line_list[0] = translator.translate(line_list[0])
            f_a.write(' '.join(map(str, line_list)) + '\n')
