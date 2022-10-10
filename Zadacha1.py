# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open("words.txt", "w") as file:
    st = file.write('авбк абвкукку бавыывыа абв вабкку абва')

with open("words.txt", 'r') as file:
    st = file.readline()

result = list(map(str, st.split()))
print(result)

result = list(filter(lambda x: 'абв' not in x, result))

print(result)
