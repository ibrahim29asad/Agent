class PokemonBlue:
    def __init__(self):
        pass
    
    @staticmethod
    def get_State(pyboyGame):
        mems = pyboyGame.memory
        current_state = {
            'player': {
                'name': mems[0xD158:0xD162],
                'X-Location': mems[0xD362],
                'Y-Location': mems[0xD361],
                'facing': mems[0xD35E],
                'badges': mems[0xD356],
            },
            'rival': {
                'name': mems[0xD34A:0xD351],
            }
        }
        return current_state
    
    @staticmethod
    def decode_gen1(word):
        converted_text= []

        mapping = {
        # Uppercase
        "128": "A", "129": "B", "130": "C", "131": "D", "132": "E", "133": "F", "134": "G",
        "135": "H", "136": "I", "137": "J", "138": "K", "139": "L", "140": "M", "141": "N",
        "142": "O", "143": "P", "144": "Q", "145": "R", "146": "S", "147": "T", "148": "U",
        "149": "V", "150": "W", "151": "X", "152": "Y", "153": "Z",
        # Lowercase
        "160": "a", "161": "b", "162": "c", "163": "d", "164": "e", "165": "f", "166": "g",
        "167": "h", "168": "i", "169": "j", "170": "k", "171": "l", "172": "m", "173": "n",
        "174": "o", "175": "p", "176": "q", "177": "r", "178": "s", "179": "t", "180": "u",
        "181": "v", "182": "w", "183": "x", "184": "y", "185": "z",
        # Numbers
        "240": "0", "241": "1", "242": "2", "243": "3", "244": "4",
        "245": "5", "246": "6", "247": "7", "248": "8", "249": "9",
        # Space
        "80": " "
        }   


        converted_text = []
        for b in word:  # iterate directly over the list
            key = str(b)
            if key in mapping:
                converted_text.append(mapping[key])
            else:
                converted_text.append("?")  # fallback for unmapped values

        return "".join(converted_text)

