from pyboy import PyBoy
from dotenv import load_dotenv
import os

load_dotenv()
# Loading the Pokemon Game from the Path
Pokemon_game = os.getenv("POKEMON_BLUE_GAME_PATH")
# pyboy = PyBoy(Pokemon_game)

# window null is used for the headless state so that the GUI is not being run 
# This improves run times 
pyboy = PyBoy(Pokemon_game, window='null')

# Runs for x frames
x = 50
for _ in range(x):
    pyboy.button('start')
    pyboy.tick()
    pyboy.button('a')
    pyboy.tick()



pyboy.stop()
print("Pokemon Blue has Finished")

