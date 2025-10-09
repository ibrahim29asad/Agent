from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv
from stable_baselines3.common.env_checker import check_env
from gymML import gymML
from NavWrap import NavWrap
import os
from dotenv import load_dotenv

load_dotenv()

def make_env():
    pokemon_game = os.getenv("POKEMON_BLUE_GAME_PATH")
    if not pokemon_game:
        raise ValueError("POKEMON_BLUE_GAME_PATH environment variable not set")
    
    env = gymML(pokemon_game)
    env = NavWrap(env)
    return env

def main():
    print("Creating environment...")
    
    # Test environment creation
    try:
        env = make_env()
        print("Environment created successfully")
        
        # Check if environment follows Gymnasium interface
        check_env(env)
        print("Environment passed compatibility check")
        
    except Exception as e:
        print(f"Error creating environment: {e}")
        return
    
    # Create vectorized environment
    print("Creating vectorized environment...")
    env = DummyVecEnv([make_env])
    
    # Initialize PPO model
    print("Initializing PPO model...")
    model = PPO(
        "MultiInputPolicy", 
        env, 
        verbose=1, 
        learning_rate=0.0003, 
        n_steps=2048, 
        batch_size=64,
        tensorboard_log="./tensorboard_logs/"
    )
    
    # Train the model
    print("Starting training...")
    try:
        model.learn(total_timesteps=50000, progress_bar=True)
        model.save("ppo_pokemon_navigation_v1")
        print("Training completed and model saved!")
        
    except Exception as e:
        print(f"Error during training: {e}")
    
    finally:
        env.close()

if __name__ == "__main__":
    main()