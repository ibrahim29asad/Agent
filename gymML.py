# Purpose of this is to create the RL Enviroment using Gymnasium by OpenAI
# Uses an imperfect Version of Markov Decision Process
#gymML.py
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
        self.Game = Game
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
                "map": spaces.Discrete(256),
                "story_flags": spaces.Box(low=0, high=255, shape=(16,), dtype=np.uint8),
                "items": spaces.Box(low=0, high=255, shape=(11,), dtype=np.uint8),
                "text_open": spaces.Discrete(2),
                "npc_flags": spaces.Box(low=0, high=255, shape=(16,), dtype=np.uint8),
            }),
            "rival": spaces.Dict({
                "name": spaces.Box(low=0, high=255, shape=(7,), dtype=np.uint8),
            })
        })




    
    def make(self):
        pass

    def reset(self, *, seed = None, options = None):
        
        super().reset(seed=seed)
        self.Emulation.end_Game()

        if options == None:
            self.Emulation = EmulatorAdaptor(self.Game)

        for _ in range(120):    
            self.Emulation.pyboy.tick()

        info = self.getInfo()
        obs = self._format_obs(PokemonBlue.get_State(self.Emulation.pyboy))
        return obs, info
        


    def getInfo(self):
        current_state = PokemonBlue.get_State(self.Emulation.pyboy)
        y, x = current_state["player"]['Y-Location'], current_state["player"]['X-Location']
        return { "x": x, "y": y }
    
    def encode_player_name(self, name_bytes, length=4):
        arr = np.array(name_bytes, dtype=np.uint8)[:length]
        if arr.shape[0] < length:
            arr = np.pad(arr, (0, length - arr.shape[0]))
        return arr

    def encode_flags(self, flags_bytes):
        flags = np.array(flags_bytes, dtype=np.uint8)
        one_hot_flags = np.zeros((len(flags), 256), dtype=np.uint8)
        for i, val in enumerate(flags):
            one_hot_flags[i, val] = 1
        return one_hot_flags.flatten()

    def normalize(self,val, max_val=255):
        return val / max_val

    
    def _format_obs(self, state):
        # player_name = self.encode_player_name(state['player']['name'])
        player_name = self.encode_player_name(state['player']['name'], length=4)
        rival_name = self.encode_player_name(state['rival']['name'], length=7)
        # npc_flags = self.encode_flags(state['player']['npc_flags'])
        npc_flags = np.array(state['player']['npc_flags'], dtype=np.uint8)  

        # Access map, story_flags, items, text_open from state['player'] instead
        return {
            "player": {
                "name": player_name,
                "X-Location": int(state['player']['X-Location']),
                "Y-Location": int(state['player']['Y-Location']),
                # "X-Location": self.normalize(state['player']['X-Location']),
                # "Y-Location": self.normalize(state['player']['Y-Location']),
                "facing": int(state['player']['facing']),
                "badges": int(state['player']['badges']),
                "map": int(state['player']['map']),
                "story_flags": np.array(state['player']['story_flags'], dtype=np.uint8),
                "items": np.array(state['player']['items'], dtype=np.uint8),
                "text_open": int(state['player']['text_open']),
                "npc_flags": npc_flags
            },
            "rival": {
                "name":rival_name,
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
        
    def debug_state(self, state):
        print(f"Map ID: {state['map']}")
        print(f"Player at ({state['player']['X-Location']}, {state['player']['Y-Location']})")
        print(f"Badges: {state['player']['badges']}")
        print(f"Dialogue open: {bool(state['dialogue_state'])}")

    def render(self):
        pass

    def off(self):
        self.Emulation.end_Game()



    # make(), Env.reset(), Env.step() and Env.render().

