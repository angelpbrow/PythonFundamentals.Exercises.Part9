import json

def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def read_all_json_files():
    pass

def write_pickle():
    # pickle.dumps()
    pass

def load_pickle():
    # pickle.loads()
    pass