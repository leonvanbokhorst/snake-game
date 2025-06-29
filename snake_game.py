#!/usr/bin/env python3
import curses
import signal
import sys
from random import randint

def signal_handler(sig, frame):
    """Handle Ctrl+C gracefully"""
    curses.endwin()
    print("\nThanks for playing Snake!")
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def create_window():
    """Initialize the game window"""
    curses.initscr()
    curses.cbreak()
    curses.noecho()
    curses.curs_set(0)
    
    # Create game window
    height, width = 22, 62
    window = curses.newwin(height, width, 0, 0)
    window.keypad(True)
    window.border(0)
    window.timeout(150)  # Game speed (lower = faster)
    
    return window

def show_instructions(window):
    """Display game instructions"""
    window.addstr(1, 2, "SNAKE GAME - Use arrow keys to move, 'q' to quit")
    window.addstr(2, 2, "Eat the food (*) to grow and increase your score!")
    window.refresh()
    curses.napms(2000)  # Show for 2 seconds

def generate_food(snake, height, width):
    """Generate food at a random location not occupied by snake"""
    while True:
        food = [randint(3, height-3), randint(2, width-3)]
        if food not in snake:
            return food

def display_score(window, score):
    """Display the current score"""
    window.addstr(0, 2, f"Score: {score}")

def game_over(window, score):
    """Display game over screen"""
    height, width = window.getmaxyx()
    msg1 = "GAME OVER!"
    msg2 = f"Final Score: {score}"
    msg3 = "Press any key to exit"
    
    window.addstr(height//2 - 1, (width - len(msg1))//2, msg1)
    window.addstr(height//2, (width - len(msg2))//2, msg2)
    window.addstr(height//2 + 1, (width - len(msg3))//2, msg3)
    window.refresh()
    window.getch()

def play_game(window):
    """Main game loop"""
    height, width = window.getmaxyx()
    
    # Show instructions
    show_instructions(window)
    window.clear()
    window.border(0)
    
    # Initialize snake in the center
    snake_y = height // 2
    snake_x = width // 2
    snake = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]
    
    # Generate initial food
    food = generate_food(snake, height, width)
    window.addch(food[0], food[1], '*')
    
    # Initial direction (moving right)
    direction = curses.KEY_RIGHT
    score = 0
    
    while True:
        # Display score
        display_score(window, score)
        
        # Get user input
        next_key = window.getch()
        
        # Handle quit
        if next_key == ord('q') or next_key == ord('Q'):
            break
            
        # Update direction (prevent reverse direction)
        if next_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
            if (next_key == curses.KEY_UP and direction != curses.KEY_DOWN) or \
               (next_key == curses.KEY_DOWN and direction != curses.KEY_UP) or \
               (next_key == curses.KEY_LEFT and direction != curses.KEY_RIGHT) or \
               (next_key == curses.KEY_RIGHT and direction != curses.KEY_LEFT):
                direction = next_key
        
        # Calculate new head position
        head = snake[0]
        new_head = [head[0], head[1]]
        
        if direction == curses.KEY_UP:
            new_head[0] -= 1
        elif direction == curses.KEY_DOWN:
            new_head[0] += 1
        elif direction == curses.KEY_LEFT:
            new_head[1] -= 1
        elif direction == curses.KEY_RIGHT:
            new_head[1] += 1
        
        # Check for collisions
        if (new_head[0] <= 0 or new_head[0] >= height-1 or
            new_head[1] <= 0 or new_head[1] >= width-1 or
            new_head in snake):
            game_over(window, score)
            break
        
        # Add new head
        snake.insert(0, new_head)
        
        # Check if food was eaten
        if new_head == food:
            score += 1
            food = generate_food(snake, height, width)
            window.addch(food[0], food[1], '*')
            # Speed up slightly as score increases
            window.timeout(max(50, 150 - score * 5))
        else:
            # Remove tail if no food eaten
            tail = snake.pop()
            window.addch(tail[0], tail[1], ' ')
        
        # Draw snake head
        window.addch(new_head[0], new_head[1], '#')
        
        # Refresh window
        window.refresh()

def main():
    """Main function"""
    try:
        window = create_window()
        play_game(window)
    except Exception as e:
        curses.endwin()
        print(f"An error occurred: {e}")
    finally:
        curses.endwin()
        print("Thanks for playing Snake!")

if __name__ == "__main__":
    main()

