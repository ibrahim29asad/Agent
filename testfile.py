
from dotenv import load_dotenv
import os
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

# Run 1000 random steps
for step in range(1000):
    action = env.action_space.sample()
    obs, reward, terminated, truncated, info = env.step(action)

    print("Sample obs:")
    for k, v in obs.items():
        print(f"  {k}: type={type(v)}, value={v}")
        if hasattr(v, "shape"):
            print(f"     shape={v.shape}, dtype={v.dtype}")

    assert env.observation_space.contains(obs), "Obs doesn't match space!"

    # Example logging if your obs dict has positions
    if isinstance(obs, dict) and "player_xy" in obs:
        if step % 100 == 0:
            print(f"Step {step}: player_xy={obs['player_xy']}")

    if terminated or truncated:
        obs, info = env.reset()

env.close()
print("✅ Finished 1000 random steps without crash")



# env = gymML(Pokemon_game)
# obs, info = env.reset()
# print(obs, info)
# obs, reward, done, trunc, info = env.step(0)
# print(obs, reward, done, trunc, info)