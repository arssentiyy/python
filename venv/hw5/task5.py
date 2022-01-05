# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def sum_str():
    try:
        with open('D:\SA\Files\my_file_5.txt', 'w+') as file_obj:
            line = input('Введите числа через пробел: ')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Возможно ошибка в файле')
    except ValueError:
        print('Неправильно набран номер или ввод')
sum_str()

