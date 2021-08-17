from states.BaseState import BaseState
import pygame, os

class Team(BaseState):
    def __init__(self, game):
        # run init function in base state
        BaseState.__init__(self, game)

        # where we store user input
        self.input = ""

        # load fonts
        self.questionfont = pygame.font.Font(os.path.join(self.game.font_dir, "Penguin-Regular.ttf"), 50)
        self.font = pygame.font.Font(os.path.join(self.game.font_dir, "STIXTwoText-Italic.ttf"), 40)


    # what do run each frame
    def update(self, dt, actions):

        # get characters
        if (self.game.actions["other"]):
            if (self.game.actions['other'] == "\b"):
                self.input = self.input[:-1]
            else:
                self.input += self.game.actions["other"]

        # if we press enter
        if (self.game.actions['enter']):

            # input validation
            if (len(self.input) >= 4):
                self.game.team = self.input
                self.game.state_stack.append(self.game.play_screen)

    # what we render to the screen
    def render(self, display):
        # fill screen with white
        display.fill((255, 255, 255))

        # draw title
        self.game.draw_text(display, "Insert Team Name", (0,0,255), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/3, self.questionfont)

        # draw input
        self.game.draw_text(display, self.input, (0,0,0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/2, self.font)