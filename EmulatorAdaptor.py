from pyboy import PyBoy
import io
import keyboard

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
        
        
    def buttonPress(self, action):
        if action not in self.controls:
            print("Cant do that boss")
            return False

        if action == "9":
            self.endGame()
            return True
        
        else:
            self.pyboy.button(self.controls[action])
            self.pyboy.tick()
            return False

        
    def SaveState(self, saved):
        with io.BytesIO() as f:
            f.seek(0)
            self.pyboy.save_state(f)
         
    
    def LoadState(self, Load):
        with io.BytesIO() as f:
            f.seek(0)
            self.pyboy.load_state(f)
        

    def run(self):
        # Let the game boot 
        for _ in range(500):
            self.pyboy.tick()

        
        print("Game booted. Ready for input.")
        
        while True:
            self.pyboy.tick()
            if keyboard.is_pressed('space'):
                print("Spacebar is pressed!")
        # while True:
        #     self.pyboy.tick()
        #     user_input = input("Enter action (1-9): ")
        #     done = self.buttonPress(user_input)
        #     if done:
        #         break

        

    # Idea is let it run until theres an input once theres an input do that input and then allow it run back 
    # to the orginal loop

    def endGame(self):
        self.pyboy.stop(False)

    
        

