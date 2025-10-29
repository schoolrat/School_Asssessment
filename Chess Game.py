import tkinter as tk

# Define board parameters
SQUARE_SIZE = 60  # Size of each square in pixels
BOARD_SIZE = 8
WINDOW_WIDTH = BOARD_SIZE * SQUARE_SIZE
WINDOW_HEIGHT = BOARD_SIZE * SQUARE_SIZE

def create_board_gui():
    """Sets up the main Tkinter window and draws the checkerboard."""
    
    # 1. Initialize the main window
    root = tk.Tk()
    root.title("Basic Chess Board")
    
    # 2. Create a Canvas widget for drawing the board
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack(padx=10, pady=10) # Add a small border around the canvas
    
    # Define colors
    color1 = "#DDBB88"  # Light square color (e.g., tan)
    color2 = "#AA5533"  # Dark square color (e.g., brown)
    
    # 3. Draw the 8x8 checkerboard pattern
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Determine the color based on the sum of row and column indices
            # (row + col) % 2 will alternate between 0 and 1
            if (row + col) % 2 == 0:
                color = color1
            else:
                color = color2
            
            # Calculate the coordinates for the top-left and bottom-right corners
            x1 = col * SQUARE_SIZE
            y1 = row * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            
            # Draw the rectangle (square)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            
            # OPTIONAL: Add algebraic notation for context (e.g., 'a8', 'h1')
            # Only label a few squares for demonstration
            if (row == 0 and col == 0) or (row == 7 and col == 7):
                 # Convert (row, col) to algebraic notation
                 file = chr(ord('a') + col)
                 rank = str(8 - row)
                 notation = file + rank
                 
                 # Place the text slightly offset
                 canvas.create_text(x1 + 10, y1 + 10, text=notation, 
                                    fill="black" if color == color1 else "white", 
                                    anchor="nw", font=('Arial', 8, 'bold'))

    # 4. Start the Tkinter event loop
    root.mainloop()

# Execute the function to display the board
if __name__ == '__main__':
    create_board_gui()