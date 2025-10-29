def create_initial_board():
    """Initializes the chess board with pieces in their starting positions."""
    # R: Rook, N: Knight, B: Bishop, Q: Queen, K: King, P: Pawn
    # Lowercase for black, Uppercase for white.
    board = [
        ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
        ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
    ]
    return board

def display_board(board):
    """Prints the chess board to the console."""
    print("   ---------------------------------")
    # Print the board from rank 8 (row 0) down to rank 1 (row 7)
    for i in range(8):
        # Algebraic rank number
        print(f" {8 - i} |", end="")
        for j in range(8):
            # Print the piece or a space, surrounded by separators
            print(f" {board[i][j]} |", end="")
        print("\n   ---------------------------------")
    
    # Print the algebraic file letters at the bottom
    print("     a   b   c   d   e   f   g   h\n")

# --- Main Program ---
# 1. Create the board
chess_board = create_initial_board()

# 2. Display the board
display_board(chess_board)

# You can test a move by directly modifying the list, 
# though a full game would require move validation logic.
# Example: Move White Pawn from e2 (index [6][4]) to e4 (index [4][4])
# chess_board[4][4] = chess_board[6][4]
# chess_board[6][4] = ' '
# display_board(chess_board)