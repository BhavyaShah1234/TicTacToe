import random

board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
moves = [1, 2, 3, 4, 5, 6, 7, 8, 9]
win = [[1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7]]
toss = ['H', 'T']
sym = ['X', 'O']
name = input('Enter your name:')
print(f'Welcome to Tic Tac Toe, {name}.')
toss_choice = input('Choose H or T:')
toss_result = random.choice(toss)
print(f'The result of the toss is {toss_result}.')
if toss_choice == toss_result:
    print('You won the toss.')
    symbol_user = input('Enter your symbol(from X and O):')
    if symbol_user == 'X':
        symbol_comp = 'O'
    if symbol_user == 'O':
        symbol_comp = 'X'
    print('You get to play first.')
    user = []
    comp = []
    running = True
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(f'{board[i][j]}\n')
            else:
                print(board[i][j], end='    ')
    while running:
        # User's turn
        if len(moves) != 0:
            position_user = int(input('Enter position to place symbol:'))
            moves.remove(position_user)
            user.append(position_user)
            user.sort()
        else:
            print("It's a draw.")
            exit(0)
        for i in range(3):
            for j in range(3):
                if board[i][j] == position_user:
                    board[i][j] = symbol_user
        # Display of board after user's turn
        for row in range(3):
            for column in range(3):
                if column == 2:
                    print(f'{board[row][column]}\n')
                else:
                    print(board[row][column], end='    ')
        # Checking winning condition after user's turn
        for i in range(0, len(user), 1):
            for j in range(i, len(user), 1):
                for k in range(j, len(user), 1):
                    if user[i] == 1 and user[j] == 2 and user[k] == 3:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 4 and user[j] == 5 and user[k] == 6:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 7 and user[j] == 8 and user[k] == 9:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 1 and user[j] == 4 and user[k] == 7:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 2 and user[j] == 5 and user[k] == 8:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 3 and user[j] == 6 and user[k] == 9:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 1 and user[j] == 5 and user[k] == 9:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 3 and user[j] == 5 and user[k] == 7:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    else:
                        pass
        # Computer's turn (if user has not won)
        if len(moves) != 0:
            position_comp = random.choice(moves)
            moves.remove(position_comp)
            comp.append(position_comp)
            comp.sort()
        else:
            print("It's a draw.")
            exit(0)
        print(f'Opponent played his symbol in {position_comp}')
        for i in range(3):
            for j in range(3):
                if board[i][j] == position_comp:
                    board[i][j] = symbol_comp
        for row in range(3):
            for column in range(3):
                if column == 2:
                    print(f'{board[row][column]}\n')
                else:
                    print(board[row][column], end='    ')
        for i in range(0, len(comp), 1):
            for j in range(i, len(comp), 1):
                for k in range(j, len(comp), 1):
                    if comp[i] == 1 and comp[j] == 2 and comp[k] == 3:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 4 and comp[j] == 5 and comp[k] == 6:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 7 and comp[j] == 8 and comp[k] == 9:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 1 and comp[j] == 4 and comp[k] == 7:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 2 and comp[j] == 5 and comp[k] == 8:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 3 and comp[j] == 6 and comp[k] == 9:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 1 and comp[j] == 5 and comp[k] == 9:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 3 and comp[j] == 5 and comp[k] == 7:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    else:
                        pass
else:
    print('You lost the toss')
    symbol_user = random.choice(sym)
    if symbol_user == 'X':
        symbol_comp = 'O'
    if symbol_user == 'O':
        symbol_comp = 'X'
    print(f'Your symbol is {symbol_user}')
    print('You play second.')
    user = []
    comp = []
    running = True
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(f'{board[i][j]}\n')
            else:
                print(board[i][j], end='    ')
    while running:
        if len(moves) != 0:
            position_comp = random.choice(moves)
            moves.remove(position_comp)
            comp.append(position_comp)
            comp.sort()
        else:
            print("It's a draw.")
            exit(0)
        print(f'Opponent played his symbol in {position_comp}')
        for i in range(3):
            for j in range(3):
                if board[i][j] == position_comp:
                    board[i][j] = symbol_comp
        for row in range(3):
            for column in range(3):
                if column == 2:
                    print(f'{board[row][column]}\n')
                else:
                    print(board[row][column], end='    ')
        for i in range(0, len(comp), 1):
            for j in range(i, len(comp), 1):
                for k in range(j, len(comp), 1):
                    if comp[i] == 1 and comp[j] == 2 and comp[k] == 3:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 4 and comp[j] == 5 and comp[k] == 6:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 7 and comp[j] == 8 and comp[k] == 9:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 1 and comp[j] == 4 and comp[k] == 7:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 2 and comp[j] == 5 and comp[k] == 8:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 3 and comp[j] == 6 and comp[k] == 9:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 1 and comp[j] == 5 and comp[k] == 9:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    elif comp[i] == 3 and comp[j] == 5 and comp[k] == 7:
                        print(f'Sorry {name}.\nYou lost.')
                        exit(0)
                    else:
                        pass
        if len(moves) != 0:
            position_user = int(input('Enter position to place symbol:'))
            moves.remove(position_user)
            user.append(position_user)
            user.sort()
        else:
            print("It's a draw.")
            exit(0)
        for i in range(3):
            for j in range(3):
                if board[i][j] == position_user:
                    board[i][j] = symbol_user
        for row in range(3):
            for column in range(3):
                if column == 2:
                    print(f'{board[row][column]}\n')
                else:
                    print(board[row][column], end='    ')
        for i in range(0, len(user), 1):
            for j in range(i, len(user), 1):
                for k in range(j, len(user), 1):
                    if user[i] == 1 and user[j] == 2 and user[k] == 3:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 4 and user[j] == 5 and user[k] == 6:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 7 and user[j] == 8 and user[k] == 9:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 1 and user[j] == 4 and user[k] == 7:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 2 and user[j] == 5 and user[k] == 8:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 3 and user[j] == 6 and user[k] == 9:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 1 and user[j] == 5 and user[k] == 9:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    elif user[i] == 3 and user[j] == 5 and user[k] == 7:
                        print(f'Congratulation {name}.\nYou won.')
                        exit(0)
                    else:
                        pass
