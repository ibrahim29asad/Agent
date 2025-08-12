# Purpose of this is to create the RL Enviroment using Gymnasium by OpenAI
# Uses an imperfect Version of Markov Decision Process
import gymnasium as gym
from EmulatorAdaptor import EmulatorAdaptor
from gymnasium import spaces

print("Imported Gym")

class gymML:
    def __init__(self, Game):
        env = gym.make('Pokemon-v1')
        print("Starting RL Enviroment")
        # Loading Emulator
        Emulation = EmulatorAdaptor(Game)
        self.controls = {
            "0": 'up',
            "1": 'down',
            "2": 'left',
            "3": 'right',
            "4": 'start',
            "5": 'select',
            "6": 'a',
            "7": 'b',
            "8": ' '
        }
        self.action_space = spaces.Discrete(9)
    
    def make(self):
        pass

    def reset(self):

        pass

    def step(self):
        pass

    def render(self):
        pass



    # make(), Env.reset(), Env.step() and Env.render().