while True:
    print_board(board)
    try:
        row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
        col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
        if row not in range(3) or col not in range(3):
            print("Invalid input. Please enter 0, 1, or 2.")
            continue
        if board[row][col] == " ":
            board[row][col] = player
            if check_winner(board):
                print_board(board)
                print("Player " + player + " wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")
    except ValueError:
        print("Invalid input. Please enter a number.")
