# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых
# пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

my_list = [i for i in range(21)]
print('Созданный список: ', my_list)
with open('text_5.txt', 'w+', encoding='utf-8') as f:
    f.write(' '.join(map(str, my_list)))
    f.seek(0)
    new_list = list(map(int, f.read().split()))
print('Сумма списка: ', sum(new_list))
