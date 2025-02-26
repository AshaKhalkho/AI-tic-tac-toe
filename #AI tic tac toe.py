#AI tic tac toe
import math
# Initial empty board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Function to print the board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

print_board(board)  # Test the board output
# Function to check if someone won
def check_winner(board):
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != ' ':
            return board[i][0]  # Row win
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != ' ':
            return board[0][i]  # Column win

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]  # Main diagonal win
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]  # Anti-diagonal win

    return None  # No winner yet
# Function to check if the board is full
def is_full(board):
    for row in board:
        if ' ' in row:
            return False  # There are empty spaces left
    return True
# Minimax function
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == 'X':  # Player wins
        return -10 + depth
    if winner == 'O':  # AI wins
        return 10 - depth
    if is_full(board):  # Draw
        return 0

    if is_maximizing:  # AI (O) wants to maximize its score
        best_score = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'  # Try move
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ' '  # Undo move
                    best_score = max(best_score, score)
        return best_score

    else:  # Player (X) wants to minimize AI’s score
        best_score = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'  # Try move
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ' '  # Undo move
                    best_score = min(best_score, score)
        return best_score
# Function for AI to find the best move
def best_move(board):
    best_score = -math.inf
    move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'  # Try move
                score = minimax(board, 0, False)
                board[i][j] = ' '  # Undo move

                if score > best_score:
                    best_score = score
                    move = (i, j)

    return move
# Game loop
def play_game():
    while True:
        print_board(board)

        # Player Move
        row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Invalid move! Try again.")
            continue

        if check_winner(board):
            print_board(board)
            print("🎉 Player Wins! 🎉")
            break
        if is_full(board):
            print_board(board)
            print("It's a Draw! 🤝")
            break

        # AI Move
        ai_move = best_move(board)
        if ai_move:
            board[ai_move[0]][ai_move[1]] = 'O'

        if check_winner(board):
            print_board(board)
            print("💻 AI Wins! 💻")
            break
        if is_full(board):
            print_board(board)
            print("It's a Draw! 🤝")
            break

# Start the game
play_game()
