import json

def load_json(filename):
    with open(filename, encoding="utf-8") as infile:
        return json.load(infile)


def write_json(filename, content):
    with open(filename, "w", encoding="utf-8") as outfile:
        json.dump(content, outfile, ensure_ascii=False, indent=4)