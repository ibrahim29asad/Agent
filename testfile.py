
from dotenv import load_dotenv
import os
from EmulatorAdaptor import EmulatorAdaptor
from gymML import gymML

load_dotenv()
Pokemon_game = os.getenv("POKEMON_BLUE_GAME_PATH")
print("Starting Pokemon Game")

# trial = EmulatorAdaptor(Pokemon_game)

# trial.run()

env = gymML(Pokemon_game)
obs, info = env.reset()
print(obs, info)
obs, reward, done, trunc, info = env.step(0)
print(obs, reward, done, trunc, info)