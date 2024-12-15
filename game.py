import pygame
import time
import random
import numpy as np

from prover import generateSolveFile
from prover import check
from prover import run_prover9

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 1000
CELL_SIZE = 190
GRID_SIZE = 3

BACKGROUND_COLOR = (40, 40, 40)
TEXT_COLOR = (255, 255, 255)
SCORE_COLOR = (40, 40, 40)

POP_WIDTH = 590
POP_HEIGHT = 40

SCORE_WIDTH = 190
SCORE_HEIGHT = 100

RESTART_SIZE = 40

pygame.init()

class Game:
    def __init__(self):
        self.initScreen()
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.current_player = 1
          
        self.cellNumber = 0
        self.game_over = False
        
        self.winner = "None"
        
        # Define scores
        self.scoreComputer = 0
        self.scoreUser = 0
        self.scoreTie = 0

        # Define images for cells
        self.empty_img = pygame.transform.scale(pygame.image.load("assets/cell-e.png"), (CELL_SIZE, CELL_SIZE))
        self.hover_img = pygame.transform.scale(pygame.image.load("assets/cell-h.png"), (CELL_SIZE, CELL_SIZE))
        self.x_img = pygame.transform.scale(pygame.image.load("assets/cell-x.png"), (CELL_SIZE, CELL_SIZE))
        self.o_img = pygame.transform.scale(pygame.image.load("assets/cell-o.png"), (CELL_SIZE, CELL_SIZE))
        
        # Define images for SCORE
        self.score_computer = pygame.transform.scale(pygame.image.load("assets/score-u.png"), (SCORE_WIDTH, SCORE_HEIGHT))
        self.score_tie = pygame.transform.scale(pygame.image.load("assets/score-t.png"), (SCORE_WIDTH, SCORE_HEIGHT))
        self.score_user = pygame.transform.scale(pygame.image.load("assets/score-c.png"), (SCORE_WIDTH, SCORE_HEIGHT))
        
        # Define images for POPUP:
        self.pop_computer= pygame.transform.scale(pygame.image.load("assets/pop-c.png"), (POP_WIDTH, POP_HEIGHT))
        self.pop_tie = pygame.transform.scale(pygame.image.load("assets/pop-t.png"), (POP_WIDTH, POP_HEIGHT))
        self.pop_user = pygame.transform.scale(pygame.image.load("assets/pop-u.png"), (POP_WIDTH, POP_HEIGHT))
        
        # Define images for RESTART BUTTON
        self.restart_button = pygame.transform.scale(pygame.image.load("assets/button-restart.png"), (RESTART_SIZE, RESTART_SIZE))
        self.restart_hover = pygame.transform.scale(pygame.image.load("assets/button-restart-hover.png"), (RESTART_SIZE, RESTART_SIZE))
        self.restart_button_pos = (20, 20)  
        
        self.font = pygame.font.Font("assets/RobotoMono-Bold.ttf", 24)
        self.fontTitle = pygame.font.Font("assets/RobotoMono-Bold.ttf", 40)

    def initScreen(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Tic Tac Toe")
        self.screen.fill(BACKGROUND_COLOR)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        hover_x, hover_y = (mouse_pos[0] - 105) // (CELL_SIZE + 10), (mouse_pos[1] - 300) // (CELL_SIZE + 10)
        
        self.screen.blit(self.score_computer, (105, 148))
        self.screen.blit(self.score_tie, (305, 148))
        self.screen.blit(self.score_user, (505, 148))
        
        for row in range(GRID_SIZE):
            for col in range(GRID_SIZE):
                x = col * (CELL_SIZE + 10) + 105
                y = row * (CELL_SIZE + 10) + 328
                if self.grid[row][col] == 0:  
                    self.screen.blit(self.empty_img, (x, y))
                elif self.grid[row][col] == 1:  
                    self.screen.blit(self.x_img, (x, y))
                elif self.grid[row][col] == 2:  
                    self.screen.blit(self.o_img, (x, y))
                if row == hover_y and col == hover_x and self.grid[row][col] == 0:
                    self.screen.blit(self.hover_img, (x, y))
        
        restart_x, restart_y = self.restart_button_pos
        if restart_x <= mouse_pos[0] <= restart_x + RESTART_SIZE and restart_y <= mouse_pos[1] <= restart_y + RESTART_SIZE:
            self.screen.blit(self.restart_hover, self.restart_button_pos)
        else:
            self.screen.blit(self.restart_button, self.restart_button_pos)

    def drawText(self):
        text_surface = self.fontTitle.render("Tic Tac Toe", True, TEXT_COLOR)
        self.screen.blit(text_surface, (268, 60))
        
    def updateScores(self):
        text_surface = self.font.render(f"{self.scoreUser:02}", True, SCORE_COLOR)
        self.screen.blit(text_surface, (186, 200))

        text_surface = self.font.render(f"{self.scoreTie:02}", True, SCORE_COLOR)
        self.screen.blit(text_surface, (386, 200))
        
        text_surface = self.font.render(f"{self.scoreComputer:02}", True, SCORE_COLOR)
        self.screen.blit(text_surface, (586, 200))


    def handle_click(self, pos):
        restart_x, restart_y = self.restart_button_pos
        if restart_x <= pos[0] <= restart_x + RESTART_SIZE and restart_y <= pos[1] <= restart_y + RESTART_SIZE:
            self.reset_game()
            return

        if not self.game_over:
            x = (pos[0] - 105) // (CELL_SIZE + 10)
            y = (pos[1] - 300) // (CELL_SIZE + 10)
            if 0 <= x < GRID_SIZE and 0 <= y < GRID_SIZE and self.grid[y][x] == 0:
                self.grid[y][x] = self.current_player
                self.cellNumber += 1
                if self.checkWinner() and not self.game_over:
                    self.winner = "X"
                    self.game_over = True
                    self.scoreUser += 1
                self.current_player = 2
                    
                    
        
                

        if not self.game_over and self.cellNumber < 9 and self.current_player == 2:
            empty_cells = [(row, col) for row in range(GRID_SIZE) for col in range(GRID_SIZE) if self.grid[row][col] == 0]
            if empty_cells:
                row, col = random.choice(empty_cells)
                self.grid[row][col] = self.current_player                  
                self.cellNumber += 1
                if self.checkWinner() and not self.game_over:
                    self.winner = "O"
                    self.game_over = True
                    self.scoreComputer += 1
                self.current_player = 1
                    
            
        if self.cellNumber == 9 and not self.game_over:
            self.current_player = 1
            if self.checkWinner():
                self.winner = "X"
                self.game_over = True
                self.scoreUser += 1
                
            
            self.current_player = 2
            
            if self.checkWinner():
                self.winner = "O"
                self.game_over = True
                self.scoreComputer += 1
                
            else:
                self.winner = "Tie"
                self.scoreTie += 1
                self.game_over = True
            
    def checkWinner(self):
        if(self.cellNumber > 3):
            generateSolveFile(self.grid, self.current_player)
            if run_prover9():
                return check()
            return False
        return False
            

    def showPopUp(self, winner):
        if winner == "X": 
            self.screen.blit(self.pop_user, (105, 268))
        elif winner == "O": 
            self.screen.blit(self.pop_computer, (105, 268))
        elif winner == "Tie": 
            self.screen.blit(self.pop_tie, (105, 268))
        if not winner == "None":
            pygame.display.flip()

    def run(self):
        running = True
        clock = pygame.time.Clock()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_over:
                        self.reset_grid()
                    else:
                        self.handle_click(pygame.mouse.get_pos())
                if event.type == pygame.KEYDOWN and self.game_over:
                    if event.key == pygame.K_r:  
                        self.reset_game()

            self.screen.fill(BACKGROUND_COLOR)
            self.draw()
            self.showPopUp(self.winner)
            self.updateScores()
            self.drawText()
            pygame.display.flip()
            clock.tick(60)
        pygame.quit()
        
    def reset_grid(self):
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.winner = "None"
        self.current_player = 1
        self.cellNumber = 0
        self.game_over = False

    def reset_game(self):
        self.grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=int)
        self.winner = "None"
        self.current_player = 1
        self.cellNumber = 0
        self.game_over = False
        self.scoreComputer = 0
        self.scoreTie = 0
        self.scoreUser = 0

if __name__ == "__main__":
    game = Game()
    game.run()
