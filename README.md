# Snake Game

A classic Snake game implementation in Python using the curses library for terminal-based gameplay.

## Features

- Terminal-based Snake game
- Arrow key controls
- Growing snake mechanics
- Score tracking
- Increasing difficulty (speed increases with score)
- Collision detection
- Food generation

## Requirements

- Python 3.x
- curses library (included in standard Python installation on Unix-like systems)

## How to Play

1. Run the game:
   ```bash
   python3 snake_game.py
   ```

2. Use arrow keys to control the snake:
   - ↑ Up arrow: Move up
   - ↓ Down arrow: Move down
   - ← Left arrow: Move left
   - → Right arrow: Move right

3. Game objective:
   - Eat the food (*) to grow your snake and increase your score
   - Avoid hitting the walls or the snake's own body
   - The game gets faster as your score increases

4. Exit the game:
   - Press 'q' or 'Q' to quit
   - Press Ctrl+C for emergency exit

## Game Controls

- **Arrow Keys**: Change snake direction
- **Q**: Quit game
- **Ctrl+C**: Emergency exit

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/leonvanbokhorst/snake-game.git
   cd snake-game
   ```

2. Run the game:
   ```bash
   python3 snake_game.py
   ```

## Game Rules

- The snake starts with 3 segments
- Eating food (*) increases the snake length by 1 segment
- The snake cannot move in the opposite direction of its current movement
- Game ends when the snake hits a wall or itself
- Score increases by 1 for each food item eaten
- Game speed increases slightly with each point scored

## Technical Details

- Written in Python 3
- Uses the curses library for terminal graphics
- Cross-platform compatible (Unix-like systems)
- Graceful error handling and cleanup

## License

This project is open source and available under the MIT License.
