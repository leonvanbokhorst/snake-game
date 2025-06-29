# Snake Game

A classic Snake game with two implementations:
- **Terminal version** (`snake_game.py`) - Using the curses library for terminal-based gameplay
- **GUI version** (`snake_game_gui.py`) - Using pygame for a modern graphical interface

## Features

### Terminal Version (`snake_game.py`)
- Terminal-based Snake game using curses
- Arrow key controls
- Growing snake mechanics
- Score tracking
- Increasing difficulty (speed increases with score)
- Collision detection
- Food generation

### GUI Version (`snake_game_gui.py`)
- Modern graphical interface using pygame
- Beautiful visual design with modern color palette
- Menu system with main menu, pause, and game over screens
- High score tracking
- Smooth animations
- Grid-based gameplay
- Multiple food colors
- Visual feedback for new high scores

## Requirements

### For Terminal Version
- Python 3.x
- curses library (included in standard Python installation on Unix-like systems)

### For GUI Version
- Python 3.x
- pygame library (`pip install pygame`)

## How to Play

### Terminal Version
1. Run the game:
   ```bash
   python3 snake_game.py
   ```

2. Use arrow keys to control the snake:
   - ↑ Up arrow: Move up
   - ↓ Down arrow: Move down
   - ← Left arrow: Move left
   - → Right arrow: Move right

3. Exit the game:
   - Press 'q' or 'Q' to quit
   - Press Ctrl+C for emergency exit

### GUI Version
1. Install pygame:
   ```bash
   pip install pygame
   ```

2. Run the game:
   ```bash
   python3 snake_game_gui.py
   ```

3. Navigate menus:
   - **SPACE**: Start game / Play again
   - **Arrow Keys**: Control snake direction
   - **P**: Pause/Resume game
   - **Q**: Quit to menu or exit

## Game Objective

- Eat the food to grow your snake and increase your score
- Avoid hitting the walls or the snake's own body
- Try to achieve the highest score possible!

## Game Controls

### Terminal Version
- **Arrow Keys**: Change snake direction
- **Q**: Quit game
- **Ctrl+C**: Emergency exit

### GUI Version
- **Arrow Keys**: Change snake direction
- **SPACE**: Start game / Play again
- **P**: Pause/Resume
- **Q**: Quit to menu / Exit

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/leonvanbokhorst/snake-game.git
   cd snake-game
   ```

2. For GUI version, install pygame:
   ```bash
   pip install pygame
   ```

3. Run your preferred version:
   ```bash
   # Terminal version
   python3 snake_game.py
   
   # GUI version
   python3 snake_game_gui.py
   ```

## Game Rules

- The snake starts with a few segments
- Eating food increases the snake length by 1 segment
- The snake cannot move in the opposite direction of its current movement
- Game ends when the snake hits a wall or itself
- **Terminal version**: Score increases by 1 per food, speed increases with score
- **GUI version**: Score increases by 10 per food, maintains consistent speed

## Technical Details

### Terminal Version
- Written in Python 3
- Uses curses library for terminal graphics
- Cross-platform compatible (Unix-like systems)
- Dynamic speed adjustment based on score
- Graceful error handling and cleanup

### GUI Version
- Written in Python 3 with pygame
- Object-oriented design with game states
- Modern visual design with grid system
- Menu system with pause functionality
- High score persistence during session
- Cross-platform GUI compatibility

## License

This project is open source and available under the MIT License.
