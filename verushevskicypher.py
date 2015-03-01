import json, argparse

def get_encode_map(file_name):
    file = open(file_name, 'r')
    file_content = json.load(file)
    file.close()
    if type(file_content) == dict:
        return file_content
    else:
        raise IOError()
    
def encode(message, encode_map):
    return '_'.join([str(encode_map[char]) for char in message])

def decode(message, encode_map):
    decode_map = {v: k for k, v in encode_map.items()}
    return ''.join([decode_map[int(code)] for code in message.split('_')])

def get_default_mapfile():
    file_dir = os.path.dirname(os.path.realpath(__file__))
    map_file = os.path.join(file_dir, 'encode_map.json')
    return map_file
    
DEFAULT_MAPFILE = get_default_mapfile()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('mode", choices=['encode', 'decode'])
    parser.add_argument('message", nargs='*')
    parser.add_argument('--mapfile', default=DEFAULT_MAPFILE)
    
    arguments = parser.parse_args()
    
    map_file = arguments.mapfile
    encode_map = get_encode_map(map_file)
    if arguments.mode == 'encode':
        print(encode(' '.join(arguments.message), encode_map))
    else:
        print(decode(' '.join(arguments.message), encode_map))
