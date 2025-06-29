#!/usr/bin/env python3
import pygame
import random
import sys
from enum import Enum

# Initialize pygame
pygame.init()
pygame.mixer.init()

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class GameState(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3
    PAUSED = 4

# Colors (modern palette)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (231, 76, 60)
GREEN = (46, 204, 113)
BLUE = (52, 152, 219)
YELLOW = (241, 196, 15)
PURPLE = (155, 89, 182)
ORANGE = (230, 126, 34)
DARK_GREEN = (39, 174, 96)
LIGHT_GRAY = (236, 240, 241)
DARK_GRAY = (52, 73, 94)
NAVY = (44, 62, 80)

# Display settings
WIDTH, HEIGHT = 900, 700
BLOCK_SIZE = 20
FPS = 12

# Initialize screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🐍 Modern Snake Game 🐍')
clock = pygame.time.Clock()

# Fonts
title_font = pygame.font.Font(None, 72)
menu_font = pygame.font.Font(None, 48)
text_font = pygame.font.Font(None, 36)
score_font = pygame.font.Font(None, 32)

class Snake:
    def __init__(self):
        self.body = [[WIDTH//2, HEIGHT//2]]
        self.direction = Direction.RIGHT
        self.grow = False
        
    def move(self):
        head = self.body[0].copy()
        
        if self.direction == Direction.UP:
            head[1] -= BLOCK_SIZE
        elif self.direction == Direction.DOWN:
            head[1] += BLOCK_SIZE
        elif self.direction == Direction.LEFT:
            head[0] -= BLOCK_SIZE
        elif self.direction == Direction.RIGHT:
            head[0] += BLOCK_SIZE
            
        self.body.insert(0, head)
        
        if not self.grow:
            self.body.pop()
        else:
            self.grow = False
    
    def change_direction(self, new_direction):
        # Prevent reversing into itself
        opposite_directions = {
            Direction.UP: Direction.DOWN,
            Direction.DOWN: Direction.UP,
            Direction.LEFT: Direction.RIGHT,
            Direction.RIGHT: Direction.LEFT
        }
        
        if new_direction != opposite_directions.get(self.direction):
            self.direction = new_direction
    
    def check_collision(self):
        head = self.body[0]
        
        # Wall collision
        if (head[0] < 0 or head[0] >= WIDTH or 
            head[1] < 0 or head[1] >= HEIGHT):
            return True
            
        # Self collision
        if head in self.body[1:]:
            return True
            
        return False
    
    def draw(self, surface):
        for i, segment in enumerate(self.body):
            color = DARK_GREEN if i == 0 else GREEN  # Head is darker
            pygame.draw.rect(surface, color, 
                           (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(surface, WHITE, 
                           (segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE), 2)

class Food:
    def __init__(self):
        self.position = self.generate_position()
        self.colors = [RED, YELLOW, ORANGE, PURPLE]
        self.color = random.choice(self.colors)
    
    def generate_position(self):
        x = random.randint(0, (WIDTH - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (HEIGHT - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        return [x, y]
    
    def respawn(self, snake_body):
        while True:
            self.position = self.generate_position()
            if self.position not in snake_body:
                self.color = random.choice(self.colors)
                break
    
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, 
                        (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE))
        pygame.draw.rect(surface, WHITE, 
                        (self.position[0], self.position[1], BLOCK_SIZE, BLOCK_SIZE), 2)

class Game:
    def __init__(self):
        self.state = GameState.MENU
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.high_score = 0
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
                
            if event.type == pygame.KEYDOWN:
                if self.state == GameState.MENU:
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                    elif event.key == pygame.K_q:
                        return False
                        
                elif self.state == GameState.PLAYING:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction(Direction.UP)
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction(Direction.DOWN)
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction(Direction.LEFT)
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction(Direction.RIGHT)
                    elif event.key == pygame.K_p:
                        self.state = GameState.PAUSED
                    elif event.key == pygame.K_q:
                        self.state = GameState.MENU
                        
                elif self.state == GameState.PAUSED:
                    if event.key == pygame.K_p:
                        self.state = GameState.PLAYING
                    elif event.key == pygame.K_q:
                        self.state = GameState.MENU
                        
                elif self.state == GameState.GAME_OVER:
                    if event.key == pygame.K_SPACE:
                        self.start_game()
                    elif event.key == pygame.K_q:
                        self.state = GameState.MENU
                        
        return True
    
    def start_game(self):
        self.state = GameState.PLAYING
        self.snake = Snake()
        self.food = Food()
        self.score = 0
    
    def update(self):
        if self.state == GameState.PLAYING:
            self.snake.move()
            
            # Check food collision
            if self.snake.body[0] == self.food.position:
                self.snake.grow = True
                self.score += 10
                self.food.respawn(self.snake.body)
                
            # Check game over
            if self.snake.check_collision():
                self.state = GameState.GAME_OVER
                if self.score > self.high_score:
                    self.high_score = self.score
    
    def draw_menu(self):
        screen.fill(NAVY)
        
        # Title
        title_text = title_font.render("🐍 SNAKE GAME 🐍", True, YELLOW)
        title_rect = title_text.get_rect(center=(WIDTH//2, HEIGHT//4))
        screen.blit(title_text, title_rect)
        
        # Instructions
        instructions = [
            "Press SPACE to start",
            "Use arrow keys to move",
            "Press P to pause",
            "Press Q to quit",
            f"High Score: {self.high_score}"
        ]
        
        for i, instruction in enumerate(instructions):
            color = WHITE if i < 4 else YELLOW
            text = menu_font.render(instruction, True, color)
            text_rect = text.get_rect(center=(WIDTH//2, HEIGHT//2 + i*50))
            screen.blit(text, text_rect)
    
    def draw_game(self):
        screen.fill(LIGHT_GRAY)
        
        # Draw grid
        for x in range(0, WIDTH, BLOCK_SIZE):
            pygame.draw.line(screen, WHITE, (x, 0), (x, HEIGHT), 1)
        for y in range(0, HEIGHT, BLOCK_SIZE):
            pygame.draw.line(screen, WHITE, (0, y), (WIDTH, y), 1)
        
        self.snake.draw(screen)
        self.food.draw(screen)
        
        # Score
        score_text = score_font.render(f"Score: {self.score}", True, DARK_GRAY)
        screen.blit(score_text, (10, 10))
        
        # High score
        high_score_text = score_font.render(f"High Score: {self.high_score}", True, DARK_GRAY)
        screen.blit(high_score_text, (WIDTH - 200, 10))
    
    def draw_pause(self):
        self.draw_game()
        
        # Pause overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(128)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        pause_text = title_font.render("PAUSED", True, WHITE)
        pause_rect = pause_text.get_rect(center=(WIDTH//2, HEIGHT//2 - 50))
        screen.blit(pause_text, pause_rect)
        
        resume_text = menu_font.render("Press P to resume", True, WHITE)
        resume_rect = resume_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 20))
        screen.blit(resume_text, resume_rect)
    
    def draw_game_over(self):
        screen.fill(DARK_GRAY)
        
        # Game Over text
        game_over_text = title_font.render("GAME OVER!", True, RED)
        game_over_rect = game_over_text.get_rect(center=(WIDTH//2, HEIGHT//3))
        screen.blit(game_over_text, game_over_rect)
        
        # Final score
        score_text = menu_font.render(f"Final Score: {self.score}", True, WHITE)
        score_rect = score_text.get_rect(center=(WIDTH//2, HEIGHT//2))
        screen.blit(score_text, score_rect)
        
        # High score
        if self.score == self.high_score and self.score > 0:
            new_record_text = text_font.render("🎉 NEW HIGH SCORE! 🎉", True, YELLOW)
            new_record_rect = new_record_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 50))
            screen.blit(new_record_text, new_record_rect)
        
        # Instructions
        restart_text = menu_font.render("Press SPACE to play again", True, WHITE)
        restart_rect = restart_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 100))
        screen.blit(restart_text, restart_rect)
        
        menu_text = text_font.render("Press Q for main menu", True, WHITE)
        menu_rect = menu_text.get_rect(center=(WIDTH//2, HEIGHT//2 + 150))
        screen.blit(menu_text, menu_rect)
    
    def draw(self):
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.PAUSED:
            self.draw_pause()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()
    
    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    game = Game()
    game.run()

