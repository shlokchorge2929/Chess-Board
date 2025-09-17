# Chess Board GUI

A clean and elegant chess board implementation using Python's tkinter library, featuring a modern cool-toned design with traditional chess colors.

## Features

- **Standard 8x8 Chess Board**: Classic alternating light and dark squares
- **Cool Color Scheme**: Modern steel blue background with dark slate accents
- **Chess Coordinates**: Proper algebraic notation (a-h columns, 1-8 rows)
- **Traditional Square Colors**: Cream/beige and dark brown squares
- **Clean Design**: Subtle borders and professional appearance
- **Responsive Layout**: Centered board with proper spacing

## Screenshots

*A beautiful chess board with cool background colors and traditional square patterns*

## Requirements

- Python 3.x
- tkinter (usually comes pre-installed with Python)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/chess-board-gui.git
cd chess-board-gui
```

2. Run the application:
```bash
python chess_board.py
```

## Usage

Simply run the script to display the chess board:

```python
python chess_board.py
```

The application will open a window displaying:
- An 8x8 chess board with alternating colored squares
- Coordinate labels (a-h for columns, 1-8 for rows)
- A cool-toned background theme

## Customization

You can easily customize the colors by modifying these variables in the `ChessBoard` class:

```python
# Background colors
self.root.configure(bg="#4682B4")  # Main window background
self.canvas = Canvas(bg="#2F4F4F")  # Canvas background

# Square colors
self.light_color = "#F0D9B5"  # Light squares
self.dark_color = "#B58863"   # Dark squares
```

## Code Structure

- `ChessBoard` class: Main application class
  - `__init__()`: Initialize the GUI and colors
  - `create_board()`: Generate the 8x8 grid of squares
  - `add_coordinates()`: Add chess notation labels
  - `run()`: Start the tkinter main loop

## Color Palette

| Element | Color | Hex Code |
|---------|-------|----------|
| Main Background | Steel Blue | #4682B4 |
| Canvas Background | Dark Slate Gray | #2F4F4F |
| Light Squares | Cream/Beige | #F0D9B5 |
| Dark Squares | Dark Brown | #B58863 |
| Borders | Saddle Brown | #8B4513 |
| Text | White | #FFFFFF |

## Future Enhancements

- [ ] Add chess piece graphics
- [ ] Implement piece movement functionality
- [ ] Add game logic for valid moves
- [ ] Include move history tracking
- [ ] Add different color themes
- [ ] Implement save/load board positions

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Created with ❤️ for chess enthusiasts and Python developers.

---

*Feel free to star ⭐ this repository if you found it helpful!*
