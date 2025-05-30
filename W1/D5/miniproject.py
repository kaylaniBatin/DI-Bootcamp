# Step 1: Representing the Game Board
def create_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Step 2: Displaying the Game Board
def display_board(board):
    print("  0   1   2")
    for i, row in enumerate(board):
        print(i, ' | '.join(row))
        if i < 2:
            print("  ---------")

# Step 3: Getting Player Input
def player_input(board, player):
    while True:
        try:
            row = int(input(f"Player {player}, enter row (0-2): "))
            col = int(input(f"Player {player}, enter column (0-2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            if board[row][col] == ' ':
                board[row][col] = player
                break
            else:
                print("That cell is already taken. Choose another.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")

# Step 4: Checking for a Winner
def check_win(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Step 5: Checking for a Tie
def check_tie(board):
    for row in board:
        if ' ' in row:
            return False
    return True

# Step 6: The Main Game Loop
def play():
    board = create_board()
    current_player = 'X'

    while True:
        display_board(board)
        player_input(board, current_player)

        if check_win(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break

        if check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Start the game
play()