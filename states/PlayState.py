from states.BaseState import BaseState
import pygame, os

class Play(BaseState):
    def __init__(self, game):
        # run init function in base state
        BaseState.__init__(self, game)

        # the question we're currently showing
        self.question = 0
        self.amount = len(self.game.questions)

        # button that's been pressed
        self.pressed = -1

        # total points accumulated in game
        self.game.total = 0

        # font
        self.font = pygame.font.Font(os.path.join(self.game.font_dir, "STIXTwoText-Italic.ttf"), 28)

        # box things
        self.red = pygame.Rect(10, self.game.GAME_HEIGHT/2, 350, 50)
        self.blue = pygame.Rect(self.game.GAME_WIDTH-360, self.game.GAME_HEIGHT/2, 350, 50)
        self.green = pygame.Rect(10, self.game.GAME_HEIGHT/2+100, 350, 50)
        self.pink = pygame.Rect(self.game.GAME_WIDTH-360, self.game.GAME_HEIGHT/2+100, 350, 50)

    def update(self, dt, actions):
        # check inputs
        if (self.game.actions["click"]):
            # answers
            if self.red.collidepoint(self.game.actions["click"]):
                self.pressed = 0
            elif self.blue.collidepoint(self.game.actions["click"]):
                self.pressed = 1
            elif self.green.collidepoint(self.game.actions["click"]):
                self.pressed = 2
            elif self.pink.collidepoint(self.game.actions["click"]):
                self.pressed = 3
            
            # check answer
            if (self.pressed != -1):
                if (self.pressed == self.game.questions[self.question][2]):
                    self.game.total += 1

                if (self.question+1 != self.amount):
                    self.question += 1
                else:
                    self.game.state_stack.append(self.game.end_screen)
                self.pressed = -1



    def render(self, display):
        # fill screen with white
        display.fill((255,255,255))

        # draw question
        self.game.draw_text(display, self.game.questions[self.question][0], (0,0,0), self.game.GAME_WIDTH/2, self.game.GAME_HEIGHT/4, self.font)

        # draw possible answers
        pygame.draw.rect(display, (255, 0, 0), self.red);
        self.game.draw_text(display, self.game.questions[self.question][1][0], (255,255,255), 185, self.game.GAME_HEIGHT/2+25, self.font)

        pygame.draw.rect(display, (0, 0, 255), self.blue);
        self.game.draw_text(display, self.game.questions[self.question][1][1], (255,255,255), self.game.GAME_WIDTH-185, self.game.GAME_HEIGHT/2+25, self.font)

        pygame.draw.rect(display, (0, 255, 0), self.green);
        self.game.draw_text(display, self.game.questions[self.question][1][2], (255,255,255), 185, self.game.GAME_HEIGHT/2+125, self.font)

        pygame.draw.rect(display, (255, 0, 255), self.pink);
        self.game.draw_text(display, self.game.questions[self.question][1][3], (255,255,255), self.game.GAME_WIDTH-185, self.game.GAME_HEIGHT/2+125, self.font)

