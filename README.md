# Agent
Battle Agent

Creating a Python Agent utilizing Reinforcment Learning to complete and then build upon to beat Mainline Gameboy Pokemon Games

System Arch.
Use PPO (Proximal Policy Optimization) to allow for movements 

Use CQL (Conservative Q-Learning) for Battle Mechanics 

Starting off with Pokemon Red/Blue - Test and Train with it as it is the smallest game of the bunch 

Possible Games:
-> Pokemon Gold/Silver
-> Pokemon LeafGreen/FireRed
-> Pokemon Alpha/Sapphire

Emulator Chosen: PyBoy by Baekalfen 
- Suprior Choice then using mGBA as mGBA is designed to play for humans
- This Emulator allows and is designed for Python Agents
#Pip install Guide for PyBoy to enter headless mode
https://pypi.org/project/pyboy/

The RAM Represents different catagroies such as names, pokemons, badges
Each game has different RAM's so its important to adapt to the game
https://datacrystal.tcrf.net/wiki/Pokémon_Red_and_Blue/RAM_map