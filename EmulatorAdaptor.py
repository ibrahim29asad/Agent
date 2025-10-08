# EmulatorAdaptor.py
from pyboy import PyBoy
import io
import keyboard
import sys, select
from PokemonBlue import PokemonBlue

class EmulatorAdaptor:
    # For now we just want basic movments 
    def __init__(self, Game):
        # self.pyboy = PyBoy(Game, window='null')
        print("Starting Emu")
        self.pyboy = PyBoy(Game)
        mems = self.pyboy.memory
        self.controls = {
            "0": 'up',
            "1": 'down',
            "2": 'left',
            "3": 'right',
            "4": 'start',
            "5": 'select',
            "6": 'a',
            "7": 'b',
            "8": None,
            "9": "io"
        }


    def button_Press(self, action):
        if action not in self.controls:
            print("Cant do that boss")
            return
        elif action == "9":
            self.Save_State()
        elif action == "8":   # no-op
            return
        else:
            print("Entered the Input: " + self.controls[action])
            for _ in range(15):
                self.pyboy.button(self.controls[action])
                self.pyboy.tick()
        
        to_print = self.pyboy.memory[0xD158:0xD162]
        new_word = PokemonBlue.decode_gen1(to_print)
        print("Players Name is "+ new_word)
        
    def Save_State(self):
        with io.BytesIO() as f:
            f.seek(0)
            self.pyboy.save_state(f)
         
    
    def Load_State(self, Load):
        with io.BytesIO(Load) as f:
            f.seek(0)
            self.pyboy.load_state(f)
        
    def get_non_blocking_input(self):
        if select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], []):
            return sys.stdin.read(1) # Read a single character
        return None
    
    def run(self):
        # Let the game boot for 8.3 seconds (500) 
        for _ in range(120):
            self.pyboy.tick()

        
        print("Game booted. Ready for input.")
        
        # while True:
        #     self.pyboy.tick()
        while True:
            char = self.get_non_blocking_input()
            if char:
                self.button_Press(char[0])
                if char == "9":
                    break
            # Do other work here
            self.pyboy.tick()
            
    # Idea is let it run until theres an input once theres an input do that input and then allow it run back 
    # to the orginal loop

    def end_Game(self):
        self.pyboy.stop(False)

    
        

