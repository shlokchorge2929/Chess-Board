import tkinter as tk
from tkinter import Canvas

class ChessBoard:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Chess Board")
        self.root.geometry("480x480")
        
        # background color 
        self.root.configure(bg="#4682B4")
        
        # Create canvas for the chess board
        self.canvas = Canvas(
            self.root, 
            width=400, 
            height=400, 
            bg="#2F4F4F",  # Dark slate gray for canvas background
            highlightthickness=2,
            highlightbackground="#1E3A5F"
        )
        self.canvas.pack(expand=True)
        
        # Chess board colors
        self.light_color = "#F0D9B5"  # Light beige/cream
        self.dark_color = "#B58863"   # Dark brown
        
        # Square size
        self.square_size = 50
        
        self.create_board()
        
    def create_board(self):
        """Create the 8x8 chess board"""
        for row in range(8):
            for col in range(8):
                # Calculate position
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size
                
                # Determine square color (alternating pattern)
                if (row + col) % 2 == 0:
                    color = self.light_color
                else:
                    color = self.dark_color
                
                # Create square
                self.canvas.create_rectangle(
                    x1, y1, x2, y2,
                    fill=color,
                    outline="#8B4513",  # Saddle brown outline
                    width=1
                )
        
        # Add coordinate labels
        self.add_coordinates()
    
    def add_coordinates(self):
        """Add chess coordinates (a-h, 1-8) to the board"""
        # Column labels (a-h)
        for col in range(8):
            letter = chr(ord('a') + col)
            x = col * self.square_size + self.square_size // 2
            y = 8 * self.square_size + 15
            self.canvas.create_text(
                x, y, 
                text=letter, 
                fill="white", 
                font=("Arial", 12, "bold")
            )
        
        # Row labels (1-8)
        for row in range(8):
            number = str(8 - row)  # Chess rows are numbered 8-1 from top to bottom
            x = -15
            y = row * self.square_size + self.square_size // 2
            self.canvas.create_text(
                x, y, 
                text=number, 
                fill="white", 
                font=("Arial", 12, "bold")
            )
    
    def run(self):
        """Start the tkinter main loop"""
        self.root.mainloop()

# Create and run the chess board
if __name__ == "__main__":
    chess_board = ChessBoard()
    chess_board.run()