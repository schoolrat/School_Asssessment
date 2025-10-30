import tkinter as tk

# Define board parameters
SQUARE_SIZE = 60
BOARD_SIZE = 8
WINDOW_WIDTH = BOARD_SIZE * SQUARE_SIZE
WINDOW_HEIGHT = BOARD_SIZE * SQUARE_SIZE

# --- Define Color Themes ---
CHESS_THEMES = {
    "wood": {
        "light": "#F0D9B5",  # Buff/Maple
        "dark": "#B58863",   # Walnut
        "title": "Classic Wood Board"
    },
    "green": {
        "light": "#FFFFFF",  # White
        "dark": "#769656",   # Dark Green (Tournament Standard)
        "title": "Tournament Green Board"
    },
    "blue": {
        "light": "#DDE6ED",  # Light Grey-Blue
        "dark": "#5D7B99",   # Slate Blue (Evening/Dark Mode)
        "title": "Evening Blue Board"
    }
    # You can add more themes here!
}

def create_board_gui(theme_name="wood"):
    """
    Sets up the main Tkinter window and draws the checkerboard
    using a selected color theme.
    """
    
    # 1. Select the colors from the defined themes
    theme = CHESS_THEMES.get(theme_name.lower(), CHESS_THEMES["wood"]) # Default to wood if theme not found
    color1 = theme["light"]
    color2 = theme["dark"]
    
    # 2. Initialize the main window
    root = tk.Tk()
    root.title(theme["title"])
    
    # 3. Create a Canvas widget
    canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
    canvas.pack(padx=10, pady=10)
    
    # 4. Draw the 8x8 checkerboard pattern
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            # Alternate colors
            color = color1 if (row + col) % 2 == 0 else color2
            
            # Calculate coordinates
            x1 = col * SQUARE_SIZE
            y1 = row * SQUARE_SIZE
            x2 = x1 + SQUARE_SIZE
            y2 = y1 + SQUARE_SIZE
            
            # Draw the square
            # Note: We set outline=color to hide the default black border
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)
            
            # OPTIONAL: Add a little color text for a visual flair on some squares
            if row == 0 and col == 0:
                 canvas.create_text(x1 + 10, y1 + 10, text=theme_name.upper(), 
                                    fill="black" if color == color1 else "white", 
                                    anchor="nw", font=('Arial', 8, 'bold'))

    # 5. Start the Tkinter event loop
    root.mainloop()

# --- Run the main program ---

# Create a Classic Wood board
# create_board_gui(theme_name="wood") 

# Create a Tournament Green board
# create_board_gui(theme_name="green") 

# Create an Evening Blue board
create_board_gui(theme_name="blue")
