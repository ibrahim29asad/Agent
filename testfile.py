#testfile.py
from dotenv import load_dotenv
import os
import csv # Added to create a Logged Record
from EmulatorAdaptor import EmulatorAdaptor
from gymML import gymML

load_dotenv()
Pokemon_game = os.getenv("POKEMON_BLUE_GAME_PATH")
print("Starting Pokemon Game")

# trial = EmulatorAdaptor(Pokemon_game)

# trial.run()

# Initialize env instead of just EmulatorAdaptor
env = gymML(Pokemon_game)


obs, info = env.reset()
# EmulatorAdaptor.wait_for_overworld()

print("Initial obs keys:", obs.keys() if isinstance(obs, dict) else type(obs))

trials = 3
rand_steps = 10
inital_training_csv = "training_2_day2.csv"
with open(inital_training_csv, 'w', newline='') as file:
    writer = csv.writer(file)
    # Getting a Player Name and Rival Name is enough information to know im done the title Screen
    writer.writerow(["Trial", "Step", "Player_name", "Player_X", 
                      "Player_Y", "Facing", "Badges", "Rival_Name" ])

    
    # Run 1000 random steps
    for tr in range(trials):
        
        obs, info = env.reset()
        for step in range(rand_steps):
            # Gives a Random Step 1-9
            action = env.action_space.sample()
            # Places it and returns the infor 
            obs, reward, terminated, truncated, info = env.step(action)
            print("Sample obs:")
            #Whats being written into the CSV File
            write_row = []
            write_row.append([tr])
            write_row.append([step])

            for k, v in obs.items():
                print(f"  {k}: type={type(v)}, value={v}")
                write_row.append([v])
                if hasattr(v, "shape"):
                    write_row.pop()
                    write_row.append([v.shape])
                    print(f"     shape={v.shape}, dtype={v.dtype}")
            writer.writerow(write_row) #Writing into the file
            # checks to see if values match up 
            assert env.observation_space.contains(obs), "Obs doesn't match space!"
            # if it fails
            if terminated or truncated:
                print(f"On the {tr} Trial and on {step} We Exited out")
                obs, info = env.reset()
                break

        # Move right 5 times, then down 3 times
    

env.close()
# Add F String
print(f"✅ Finished {rand_steps} random steps {trials} times without crash")



# env = gymML(Pokemon_game)
# obs, info = env.reset()
# print(obs, info)
# obs, reward, done, trunc, info = env.step(0)
# print(obs, reward, done, trunc, info)