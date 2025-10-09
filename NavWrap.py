import gymnasium as gym
from gymnasium import Wrapper
import numpy as np

class NavWrap(Wrapper):
    def __init__(self, env):
        super().__init__(env)
        self.target_locations = [
            (10, 10),  # Example: Route 1 coordinates
            (5, 8),    # Pallet Town
            (12, 15)   # Viridian City
        ]
        self.current_target = 0
        self.prev_state = None
        
    def reset(self, **kwargs):
        obs, info = super().reset(**kwargs)
        self.current_target = 0
        self.prev_state = self.get_current_state()
        return obs, info
        
    def get_current_state(self):
        # Get current position from info or observation
        if hasattr(self.env, 'getInfo'):
            info = self.env.getInfo()
            return (info.get('x', 0), info.get('y', 0))
        return (0, 0)
        
    def step(self, action):
        obs, reward, terminated, truncated, info = self.env.step(action)
        
        # Navigation-specific reward
        current_pos = self.get_current_state()
        target_pos = self.target_locations[self.current_target]
        
        # Calculate Manhattan distance
        distance = abs(current_pos[0] - target_pos[0]) + abs(current_pos[1] - target_pos[1])
        
        # Negative reward based on distance (closer = better)
        nav_reward = -distance * 0.01
        
        # Target reached
        if distance <= 2:  # Allow 2 tile proximity
            nav_reward += 5.0
            self.current_target = (self.current_target + 1) % len(self.target_locations)
            print(f"Target reached! Moving to next target: {self.target_locations[self.current_target]}")
            
        reward += nav_reward
        
        # Add small penalty for standing still
        if self.prev_state == current_pos:
            reward -= 0.05
            
        self.prev_state = current_pos
        return obs, reward, terminated, truncated, info