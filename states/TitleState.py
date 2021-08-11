from states.BaseState import BaseState
import pygame, os

class Title(BaseState): # create class called Title that inherits from BaseState

    # When title object is created
    def __init__(self, game):
        # run init function in Base State
        BaseState.__init__(self, game)

        self.largefont = pygame.font.Font(os.path.join(self.game.font_dir, "Penguin-Regular.ttf"), 80)
    
    # what do run each frame
    def update(self, dt, actions):
        # if we press enter
        if (actions["enter"]):
            self.game.state_stack.append(self.game.play_screen)


    # what we display to the screen
    def render(self, display):
        # for now just print a white background
        display.fill((255, 255, 255))

        # print text
        self.game.draw_text(display, "QUIZ", (0,0,0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/4, self.largefont)
        
    
