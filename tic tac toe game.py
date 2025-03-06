def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False
def tic_tac_toe():
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print("Use numbers 1-9 to place your mark.")
    print_board(board)
    for _ in range(9):
        print(f"Player {player}'s turn")
        while True:
            try:
                move = int(input("Enter a number (1-9): ")) - 1
                if 0 <= move <= 8 and board[move] not in ["X", "O"]:
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Enter a number between 1 and 9.")
        board[move] = player
        print_board(board)
        if check_winner(board, player):
            print(f"Player {player} wins!")
            return
        player = "O" if player == "X" else "X"
    print("It's a draw!")
tic_tac_toe()