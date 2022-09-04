import json

name = input("Имя: ")
phone = input("Телефон: ")

def create_json():
    json_data = [{
        "name": name,
        "phone": phone
    }]
    with open('users.json', 'w') as file:
        file.write(json.dumps(json_data, indent=2, ensure_ascii=False))
create_json()

def add_to_json():
    json_data = {
         "name": name,
         "phone": phone,
    }
    data = json.load(open("users.json"))
    data.append(json_data)
    with open("users.json", "w") as file:
        json.dump(data, file, indent=2, ensure_ascii=False)

add_to_json()
