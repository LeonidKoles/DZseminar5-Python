# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.


from asyncore import write
import re




with open("Erlcoding.txt", "w") as data:
    data.write(input())

with open("erlcoding.txt", "r") as data:
    st = data.read()

#st = 'aaaaasssdff ggg ge'
i = 0
result = ''
while(i <=len(st) - 1):
    count = 1
    ch = st[i]
    j = i
    while j < len(st) - 1:
        if st[j] == st[j + 1]:
            count += 1
            j += 1
        else:
            break
    result = result + str(count) + ch
    i = j + 1

print(result)

with open("ERLuncoding.txt", "w") as data:
    data.write(result)

#  раскодировка


with open("ERLuncoding.txt", "r") as f:
    uncoding_str = f.read()

unpack = ''
i = 0
j = 0

while i <= len(uncoding_str) - 1:
    cou = int(uncoding_str[i])
    word = uncoding_str[i +1]

    for j in range(cou):
        unpack += word
        j += 1
    i += 2

print(unpack)



