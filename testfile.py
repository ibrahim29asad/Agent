
from dotenv import load_dotenv
import os
from EmulatorAdaptor import EmulatorAdaptor

load_dotenv()
Pokemon_game = os.getenv("POKEMON_BLUE_GAME_PATH")
print("Starting Pokemon Game")

trial = EmulatorAdaptor(Pokemon_game)

trial.run()