from sys import argv
encode_map = {
    "a": 7,
    "b": 4,
    "v": 20,
    "g": 50,
    "d": 9,
    "e": 24,
    "z": 51,
    "i": 22,
    "j": 17,
    "k": 33,
    "l": 12,
    "m": 21,
    "n": 27,
    "o": 5,
    "p": 3,
    "r": 8,
    "s": 18,
    "t": 44,
    "u": 39,
    "c": 13,
    " ": 0,
    }
decode_map = {v: k for k, v in encode_map.items()}


def encode(s):
    return "_".join([str(encode_map[char]) for char in s])


def decode(s):
    return "".join([decode_map[int(code)] for code in s.split("_")])

if __name__ == "__main__":
    if argv[1] == "encode":
        print encode(" ".join(argv[2:]))
    elif argv[1] == "decode":
        print decode(argv[2])
