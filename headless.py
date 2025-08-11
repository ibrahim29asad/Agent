from pyboy import PyBoy
from dotenv import load_dotenv
import os

load_dotenv()
# Loading the Pokemon Game from the Path
Pokemon_game = os.getenv("POKEMON_BLUE_GAME_PATH")

# window null is used for the headless state so that the GUI is not being run 
# This improves run times 
# pyboy = PyBoy(Pokemon_game, window='null')

pyboy = PyBoy(Pokemon_game)

# while pyboy.tick():
#     pyboy.button_press('a')
#     pyboy.button_press('start')
    # pass
while True:
    pyboy.button('a') # Press button 'a' and release after `pyboy.tick()`
    pyboy.tick()
    pyboy.button('start') # Press button 'a' and release after `pyboy.tick()`
    pyboy.tick()
pyboy.stop()

print("Pokemon Blue has Started")


