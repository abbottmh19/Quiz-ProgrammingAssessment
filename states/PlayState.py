from states.BaseState import BaseState
import pygame, os

class Play(BaseState):
    def __init__(self, game):
        # run init function in base state
        BaseState.__init__(self, game)

        # the question we're currently showing
        self.question = 0
        self.amount = len(self.game.questions)

        # font
        self.font = pygame.font.Font(os.path.join(self.game.font_dir, "STIXTwoText-Italic.ttf"), 40)

    def update(self, dt, actions):
        # check inputs
        if (self.game.actions["enter"]):
            if (self.question < self.amount-1):
                self.question += 1


    def render(self, display):
        # fill screen with white
        display.fill((255,255,255))

        self.game.draw_text(display, self.game.questions[self.question][0], (0,0,0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/2, self.font)