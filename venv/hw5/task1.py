# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

new_text = input('Введите данные для записи в файл: ')
new_text.strip(new_text)

f_new = open("D:\SA\Files\my_file.txt", "w")
f_new.write(new_text + "\n")

while new_text != '':
    new_text = input('Введите данные для записи в файл: ')
    new_text.strip(new_text)
    f_new.write(new_text + "\n")



