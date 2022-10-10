# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая 
# ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно 
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему 
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все 
# конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint


plyer_1 = input('Введите имя первого игрока ')
plyer_2 = input('Введите имя второго игрока ')

print(f'Добро позаловать в игру {plyer_1} и {plyer_2}')
print('Проводится жеребьевка')
start_point = 145
max_step = 28
last_plyer = 0
draw = randint(1,2)

if draw < 2:
    first_plyer = plyer_1
    second_plyer = plyer_2
    print(f'Начинает {plyer_1}')
else:
    first_plyer = plyer_2
    second_plyer = plyer_1
    print(f'Начинает {plyer_2}')

print(draw)
while start_point > max_step:
    motion_plyer_1 = int(input(f'{first_plyer} Введите количество изымаемых конфет\n'))
    if motion_plyer_1 > max_step:
        print('Нарушены правила')
    else:
        start_point -= motion_plyer_1
        last_plyer += 1

    motion_plyer_2 = int(input(f'{second_plyer} Введите количество изымаемых конфет\n'))
    if motion_plyer_2 > max_step:
        print('Нарушены правила')
    else:
        start_point -= motion_plyer_2
        last_plyer -= 1

if last_plyer == 1:
    print(f'Попедил {second_plyer}')
else:
    print(f'Попедил {first_plyer}')
