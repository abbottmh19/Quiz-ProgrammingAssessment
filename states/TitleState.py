from states.BaseState import BaseState
import pygame, os

class Title(BaseState): # create class called Title that inherits from BaseState

    # When title object is created
    def __init__(self, game):
        # run init function in Base State
        BaseState.__init__(self, game)

        # font for giant QUIZ title
        self.largefont = pygame.font.Font(os.path.join(self.game.font_dir, "Penguin-Regular.ttf"), 80)
        self.smallfont = pygame.font.Font(os.path.join(self.game.font_dir, "Penguin-Regular.ttf"), 40)

        # currently selected option
        self.selected = 1
    
    # what do run each frame
    def update(self, dt, actions):
        # if we press enter
        if (actions["enter"]):
            if (self.selected == 1):
                self.game.state_stack.append(self.game.team_screen)
            elif (self.selected == 2):
                self.game.running = False
        
        # cycle between options with up and down arrows
        if (actions["up"]):
            if (self.selected > 1):
                self.selected -= 1
        if (actions["down"]):
            if (self.selected < 2):
                self.selected += 1

    # what we display to the screen
    def render(self, display):
        # for now just print a white background
        display.fill((255, 255, 255))

        # print title
        self.game.draw_text(display, "QUIZ", (0,0,0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/4, self.largefont)

        # print options
        if (self.selected == 1):
            self.game.draw_text(display, "start", (255,0,255), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/3+30, self.smallfont)
            self.game.draw_text(display, "quit", (0,0,0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/3+80, self.smallfont)
        else:
            self.game.draw_text(display, "start", (0,0,0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/3+30, self.smallfont)
            self.game.draw_text(display, "quit", (255, 0, 255), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/3+80, self.smallfont)
        
        
    
