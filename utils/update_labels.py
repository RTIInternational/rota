import json
from pathlib import Path
from copy import copy

config = json.loads(Path("config.json").read_text())
code_map = json.loads(Path("code_map.json").read_text())  # label : ID
code_map_inv = {v: k for k, v in code_map.items()}  # id : label

code_map_inv_str = {str(k): str(v) for k, v in code_map_inv.items()}
code_map_str = {str(v): str(k) for k, v in code_map.items()}
config["id2label"] = code_map_inv_str
config["label2id"] = code_map

Path("config.json").write_text(json.dumps(config, indent=4))
