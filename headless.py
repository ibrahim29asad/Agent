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
x = 50000
for _ in range(x):
    pyboy.button('start')
    pyboy.tick()
    pyboy.button('a')
    pyboy.tick()


# Read 16 bytes from RAM starting at 0xC000 (example)
ram_bytes = pyboy.memory[0xC000:0xC010]
print("RAM bytes at 0xC000-0xC00F:", ram_bytes)
hp = pyboy.memory[0xD163]
money = pyboy.memory[0xD16E] * 256 + pyboy.memory[0xD16F]
print(f"Player HP: {hp}")
print(f"Player Money: {money}")

pyboy.stop()
print("Pokemon Blue has Finished")

