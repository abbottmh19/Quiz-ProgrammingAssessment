import os, pygame, time

from states.TitleState import Title
from states.TeamState import Team

# main class
class Game():
    # what to do when the game first loads
    def __init__(self):
        pygame.init() # initialize pygame

        # two seperate GAME and SCREEN resolutions
        # this is done because the user may need to resize their window
        # and have a GAME resolution seperate allows everything to resize properly
        self.GAME_WIDTH,self.GAME_HEIGHT = 800,600
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 800,600

        # what we actually display to the screen (game_canvas is applied over-top of this)
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))

        # this canvas gets overlayyed against the game screen
        # this allows for dynamic resizing
        self.game_canvas = pygame.Surface((self.GAME_WIDTH, self.GAME_HEIGHT))

        # for use in game loop
        self.running = True

        # for frame-rate independence
        self.dt, self.prev_time = 0, 0

        # for inputs
        self.actions = {"up" : False, "down" : False, "enter" : False, "other" : False}

        # state machine runs functions from object at top of this stack
        self.state_stack = []

        # team name (gets inputted later)
        self.team = "unamed"

        # load componants
        self.load_assets()
        self.load_states()
    
    # loads game assets (sprites, fonts, sounds, music, etc)
    def load_assets(self):
        self.assets_dir = os.path.join("assets") # where to look for assets in game folder 
        self.font_dir = os.path.join(self.assets_dir, "fonts") # where within the assets folder to find fonts
    
    # loads game states
    def load_states(self):
        self.title_screen = Title(self)
        self.team_screen = Team(self)
        self.state_stack.append(self.title_screen)

    # game loop (function that runs each frame)
    def game_loop(self):
        self.get_dt()
        self.get_events()
        self.update()
        self.render()
        self.reset_keys()

    # get inputs
    def get_events(self):
        for event in pygame.event.get():
            # if I quit the game (like pressing X or clicking quit or smthn)
            if event.type == pygame.QUIT:
                self.running = False
            
            # if i press a key down
            if event.type == pygame.KEYDOWN:
                # if the key is ESCAPE
                if event.key == pygame.K_ESCAPE:
                    self.reset_values()
                    self.load_states()

                # if the key is ENTER
                if event.key == pygame.K_RETURN:
                    self.actions['enter'] = True
                # if the key is an up or down arrow
                elif event.key == pygame.K_UP:
                    self.actions['up'] = True
                elif event.key == pygame.K_DOWN:
                    self.actions['down'] = True
                else:
                    self.actions['other'] = event.unicode

    
    # get deltatime (for framerate independence)
    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    # run this each frame
    def update(self):
        # call update function of state on top of stack
        self.state_stack[-1].update(self.dt, self.actions) 
    
    # draw to the screen
    def render(self):
        # run the render function of the state on top of stack
        self.state_stack[-1].render(self.game_canvas)

        # apply game_canvas over screen and display screen
        self.screen.blit(pygame.transform.scale(self.game_canvas, (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()

    # function to print background
    def print_bg(self, surface, image):
        surface.blit(image, (0,0))

    # function to display text to the screen
    def draw_text(self, surface, text, color, x, y, font):
        text_surface = font.render(text, True, color)
        #text_surface.set_colorkey((0,0,0)) # last line of defense
        text_rect = (text_surface.get_rect())
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)

    # function to reset all relevant variables
    def reset_values(self):
        self.state_stack = []
    
    # function to set all actions to false
    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False

# make sure this is the main file being run and then repeat the game_loop function
if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()