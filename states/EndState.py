from states.BaseState import BaseState
import pygame, os

class End(BaseState):
    def __init__(self, game):
        # run init function in base state
        BaseState.__init__(self, game)

        # font
        self.font = pygame.font.Font(os.path.join(self.game.font_dir, "Starjedi.ttf"), 80)

    # what we render to the screen
    def render(self, display):
        # fill screen with white
        display.fill((255, 255, 255))

        # draw title
        self.game.draw_text(display, str(self.game.total) + "/" + str(len(self.game.questions)), (255,0,255), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/3, self.font)

        self.game.draw_text(display, "Press Escape", (0,0,0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/2, self.font);
