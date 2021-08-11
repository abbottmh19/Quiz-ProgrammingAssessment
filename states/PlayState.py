from states.BaseState import BaseState
import pygame, os

class Play(BaseState):
    def __init__(self, game):
        # run init function in base state
        BaseState.__init__(self, game)

    # what do run each frame
    def update(self, dt, actions):
        pass

    # what we render to the screen
    def render(self, display):

        # fill screen with white
        display.fill((255, 255, 255))