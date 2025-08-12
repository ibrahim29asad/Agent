from pyboy import PyBoy
import io
import keyboard
import sys, select

class EmulatorAdaptor:
    # For now we just want basic movments 
    def __init__(self, Game):
        # pyboy = PyBoy(Game, window='null')
        print("Starting Emu")
        self.pyboy = PyBoy(Game)
        
        self.controls = {
            "1": 'up',
            "2": 'down',
            "3": 'left',
            "4": 'right',
            "5": 'start',
            "6": 'select',
            "7": 'a',
            "8": 'b',
            "9": 'end'
        }
        
        
    def button_Press(self, action):
        if action not in self.controls:
            print("Cant do that boss")
            return
        elif action == "9":
            self.end_Game()
        else:
            print("Entered the Input: " + self.controls[action])
            for _ in range(15):
                self.pyboy.button(self.controls[action])
                self.pyboy.tick()

        
    def Save_State(self, saved):
        with io.BytesIO() as f:
            f.seek(0)
            self.pyboy.save_state(f)
         
    
    def Load_State(self, Load):
        with io.BytesIO() as f:
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
                self.button_Press(char)
                if char == "9":
                    break
            # Do other work here
            self.pyboy.tick()
            
    # Idea is let it run until theres an input once theres an input do that input and then allow it run back 
    # to the orginal loop

    def end_Game(self):
        self.pyboy.stop(False)

    
        

