from PIL import Image, ImageDraw, ImageFont
import os

def generate_chess_piece_images(output_dir="chess_pieces", square_size=60):
    """
    Generates simple chess piece images using Unicode characters.
    Each piece will be a square image with a clear background.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Unicode characters for chess pieces
    # White pieces
    pieces_white = {
        'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙'
    }
    # Black pieces
    pieces_black = {
        'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
    }

    all_pieces = {**pieces_white, **pieces_black} # Combine for iteration

    # Try to load a font that supports chess symbols.
    # Common system fonts like Arial Unicode MS, Segoe UI Symbol,
    # or Noto Color Emoji might work.
    # You might need to specify a full path for system fonts, e.g.,
    # font_path = "/System/Library/Fonts/Supplemental/Arial Unicode.ttf" (macOS)
    # font_path = "C:/Windows/Fonts/segoeuis.ttf" (Windows, for Segoe UI Symbol)
    # For better cross-platform compatibility, consider packaging a font file
    # or using a more robust font loading mechanism.
    try:
        font_size = int(square_size * 0.7) # Adjust font size relative to square
        # Using a default font, you might need to change 'arial.ttf'
        # to a font installed on your system that supports chess symbols.
        # If 'arial.ttf' doesn't work, try commenting it out or replacing.
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        print("Warning: Could not load 'arial.ttf'. Using default PIL font, "
              "which may not display chess symbols correctly.")
        font = ImageFont.load_default()
        font_size = int(square_size * 0.7) # default font doesn't scale well
    
    print(f"Generating piece images in '{output_dir}/'...")

    for piece_code, unicode_char in all_pieces.items():
        # Create a transparent image
        img = Image.new('RGBA', (square_size, square_size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)

        # Determine text color (black for white pieces, white for black pieces for contrast)
        text_fill_color = "black" if piece_code.isupper() else "white"
        
        # Calculate text bounding box to center the text
        bbox = draw.textbbox((0, 0), unicode_char, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]

        # Center the text
        x = (square_size - text_width) / 2 - bbox[0]
        y = (square_size - text_height) / 2 - bbox[1]
        
        draw.text((x, y), unicode_char, font=font, fill=text_fill_color)

        # Save the image
        filename = os.path.join(output_dir, f"{piece_code}.png")
        img.save(filename)
        print(f"Generated: {filename}")

    print("Image generation complete.")

# --- Run the script ---
if __name__ == "__main__":
    generate_chess_piece_images(square_size=60) # Adjust square_size to match your Tkinter board

