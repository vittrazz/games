def print_board(board):
    print("-------------")
    for i in range(3):
        print(f"| {board[i*3]} | {board[i*3+1]} | {board[i*3+2]} |")
        print("-------------")

def check_win(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # строки
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # столбцы
        [0, 4, 8], [2, 4, 6]              # диагонали
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def is_draw(board):
    return all(cell != " " for cell in board)

def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"

    while True:
        print_board(board)
        try:
            move = int(input(f"Игрок {current_player}, введите номер клетки (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Неверный ход! Попробуйте снова.")
                continue
        except ValueError:
            print("Введите число от 1 до 9!")
            continue

        board[move] = current_player

        if check_win(board, current_player):
            print_board(board)
            print(f"Игрок {current_player} победил!")
            break

        if is_draw(board):
            print_board(board)
            print("Ничья!")
            break

        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()