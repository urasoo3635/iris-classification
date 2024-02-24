import json

def load_json(file_path):
    """jsonを読み込む
    """
    with open(file_path, 'r') as file:
        json_dict = json.load(file)
        
    return json_dict