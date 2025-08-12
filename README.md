# Agent
Battle Agent

Creating a Python Agent utilizing Reinforcment Learning to complete and then build upon to beat Mainline Gameboy Pokemon Games

System Arch.
Use Gymnasium by OpenAI which is an API to create the RL (Reinforcment Learning) Enviroment
https://gymnasium.farama.org/index.html
pip install gymnasium

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
pip install pyboy

The RAM Represents different catagroies such as names, pokemons, badges
Each game has different RAM's so its important to adapt to the game
https://datacrystal.tcrf.net/wiki/Pokémon_Red_and_Blue/RAM_map


*** 60 frames is one Second ***


Used Select Module as User Input is blocking and Select allows the option to blick or not by choosing a 0 value


# High Level Explination:
Building a self-learning AI agent that plays Pokémon (a mainline game with story + post-game content) like a human starting from scratch, but without explicit instructions for battle decisions, item use, or capture strategy.

It will:

Learn only from its own play experience, not from pre-trained online models.
Begin with no game knowledge — discovering mechanics, rules, and strategies as it goes.
Adapt to in-game AI behavior by observing how NPC trainers and wild Pokémon act, then incorporating those patterns into its decision-making.
Develop its own risk/reward system for battles, resource use, training, and capturing Pokémon.
Persist knowledge between runs so it can replay the game better and apply its learned strategy to new Pokémon games or improve its times.
Be trained using reinforcement learning (using PPO and CQL) using my M2 Pro’s GPU for simulation and training.
Essentially — this is an autonomous Pokémon-playing RL system with long-term memory, designed to improve over time, adapt to opponents, and handle both main story and post-game content without human intervention.


To Run it:
pip install gymnasium
pip install pyboy