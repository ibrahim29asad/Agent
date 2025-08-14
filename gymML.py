# Purpose of this is to create the RL Enviroment using Gymnasium by OpenAI
# Uses an imperfect Version of Markov Decision Process
import gymnasium as gym
from EmulatorAdaptor import EmulatorAdaptor
from PokemonBlue import PokemonBlue
from gymnasium import spaces
import numpy as np

print("Imported Gym")

class gymML(gym.Env):
    def __init__(self, Game):
        print("Starting RL Enviroment")
        # Loading Emulator
        self.Emulation = EmulatorAdaptor(Game)
        self.controls = {
            "0": 'up',
            "1": 'down',
            "2": 'left',
            "3": 'right',
            "4": 'start',
            "5": 'select',
            "6": 'a',
            "7": 'b',
            "8": None
        }
        self.action_space = spaces.Discrete(9)
        self.Emulation.pyboy.tick() 
        # this is what is being looked at those Values in specific 
        self.observation_space = spaces.Dict({
            "player": spaces.Dict({
                "name": spaces.Box(low=0, high=255, shape=(4,), dtype=np.uint8),
                "X-Location": spaces.Discrete(256),
                "Y-Location": spaces.Discrete(256),
                "facing": spaces.Discrete(256),
                "badges": spaces.Discrete(256),
            }),
            "rival": spaces.Dict({
                "name": spaces.Box(low=0, high=255, shape=(7,), dtype=np.uint8),
            })
        })


    
    def make(self):
        pass

    def reset(self, *, seed = None, options = None):
        
        super().reset(seed=seed)
        
        for _ in range(120):    
            self.Emulation.pyboy.tick()

        info = self.getInfo()
        obs = self._format_obs(PokemonBlue.get_State(self.Emulation.pyboy))
        return obs, info
        


    def getInfo(self):
        current_state = PokemonBlue.get_State(self.Emulation.pyboy)
        x, y = current_state["player"]['Y-Location'], current_state["player"]['X-Location']
        return { "x": x, "y": y }
    
    # Still need to format it from the get_State
    def _format_obs(self, state):
        return {
            "player": {
                "name": np.array(state['player']['name'], dtype=np.uint8),
                "X-Location": int(state['player']['X-Location']),
                "Y-Location": int(state['player']['Y-Location']),
                "facing": int(state['player']['facing']),
                "badges": int(state['player']['badges']),
            },
            "rival": {
                "name": np.array(state['rival']['name'], dtype=np.uint8),
            }
        }

    def step(self, action):
        # So we call the have the action 
        reward = 0
        
        self.Emulation.button_Press(str(action))

        for _ in range(60):    
            self.Emulation.pyboy.tick()

        # Update Reward based on if something happend with the RAM Values
        # for now just return 0
        obs = self._format_obs(PokemonBlue.get_State(self.Emulation.pyboy))
        # obs = spaces.Dict({
        #     "player": spaces.Dict({
        #         "name": temp_obs['player']['name'],
        #         "X-Location": temp_obs['player']['X-Location'],
        #         "Y-Location": temp_obs['player']['Y-Location'],
        #         "facing": temp_obs['player']['facing'],
        #         "badges": temp_obs['player']['badges'],
        #     }),
        #     "rival": spaces.Dict({
        #         "name": temp_obs['rival']['name'],
        #     })
        # })
        terminated = False # did it quit
        truncated = False # did the objectve pass
        info = self.getInfo()

        return obs, reward, terminated, truncated, info
        

    def render(self):
        pass

    def off(self):
        self.Emulation.end_Game()


    # make(), Env.reset(), Env.step() and Env.render().