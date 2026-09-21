import random

board = [" "] * 9

def display_board():
    print()
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("---+---+---")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print()

def check_winner(player):
    winning_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    ]

    for a, b, c in winning_positions:
        if board[a] == player and board[b] == player and board[c] == player:
            return True

    return False

def board_full():
    return " " not in board

def computer_move():
    empty_positions = []

    for i in range(9):
        if board[i] == " ":
            empty_positions.append(i)

    if empty_positions:
        position = random.choice(empty_positions)
        board[position] = "O"

print("TIC-TAC-TOE GAME")
print("You are X and Computer is O")

while True:
    display_board()

    try:
        position = int(input("Enter position (1-9): "))
    except ValueError:
        print("Please enter a number.")
        continue

    if position < 1 or position > 9:
        print("Enter a position between 1 and 9.")
        continue

    position = position - 1

    if board[position] != " ":
        print("Position already occupied.")
        continue

    board[position] = "X"

    if check_winner("X"):
        display_board()
        print("You Win!")
        break

    if board_full():
        display_board()
        print("Game Draw!")
        break

    computer_move()

    if check_winner("O"):
        display_board()
        print("Computer Wins!")
        break

    if board_full():
        display_board()
        print("Game Draw!")
        break