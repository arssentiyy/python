# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

def word_count(string):
    return(len(string.strip().split(" ")))


f = open('D:\SA\Files\my_file_2.txt', encoding='utf-8', errors='ignore')
count = sum(1 for line in f)
print(count)

f = open('D:\SA\Files\my_file_2.txt', encoding='utf-8', errors='ignore')
while True:
    line = f.readline()
    if not line:
        break

    print(word_count(line.strip()))

f.close()
