import json 

def save_json(path,json_data):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(json_data,f,ensure_ascii=False,indent=2)

def read_json(path):
    with open(path,"r",encoding="utf-8") as f:
        return json.load(f)


