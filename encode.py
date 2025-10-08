import numpy as np

def encode_player_name(name_bytes):
    arr = np.array(name_bytes, dtype=np.uint8)[:4]
    if arr.shape[0] < 4:
        arr = np.pad(arr, (0, 4 - arr.shape[0]))
    return arr

def encode_flags(flags_bytes):
    # Convert each byte into a one-hot vector
    flags = np.array(flags_bytes, dtype=np.uint8)
    one_hot_flags = np.zeros((len(flags), 256), dtype=np.uint8)
    for i, val in enumerate(flags):
        one_hot_flags[i, val] = 1
    return one_hot_flags.flatten()
