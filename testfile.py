
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
            action = env.action_space.sample()
            obs, reward, terminated, truncated, info = env.step(action)
            print("Sample obs:")
            #Write into 
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
            writer.writerow(write_row)
            assert env.observation_space.contains(obs), "Obs doesn't match space!"

            if terminated or truncated:
                print(f"On the {tr} Trial and on {step} We Exited out")
                obs, info = env.reset()
                break

env.close()
# Add F String
print(f"✅ Finished {rand_steps} random steps {trials} times without crash")



# env = gymML(Pokemon_game)
# obs, info = env.reset()
# print(obs, info)
# obs, reward, done, trunc, info = env.step(0)
# print(obs, reward, done, trunc, info)