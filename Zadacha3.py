# Создайте программу для игры в ""Крестики-нолики"".

board = list(range(1, 10))

win_comb = [[0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6]]


def print_board():
    print(board[0], end = " ")
    print(board[1], end = " ")
    print(board[2])

    print(board[3], end = " ")
    print(board[4], end = " ")
    print(board[5])

    print(board[6], end = " ")
    print(board[7], end = " ")
    print(board[8])

def step_player(step, symbol):
    ind = board.index(step)
    board[ind] = symbol

def res():
    win = ""

    for i in win_comb:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win = first_player + " X"
        if board[i[0]] == "0" and board[i[1]] == "0" and board[i[2]] == "0":
            win = second_player + " 0"
    return win
first_player = input('Первый игрок, укажите свое имя\n')
second_player = input('Второй игрок, укажите свое имя\n')
game_finish = False
player1 = True

while game_finish == False:
    print_board

    if player1 == True:
        symbol = "X"
        step = int(input(f'{first_player}, ваш ход '))
    else:
        symbol = '0'
        step = int(input(f'{second_player}, ваш ход '))

    step_player(step, symbol)
    win = res()

    if win != "":
        game_finish = True
    else:
        game_finish = False
    player1 = not(player1)
    print_board()

print_board()
print('Победил', win)
        

