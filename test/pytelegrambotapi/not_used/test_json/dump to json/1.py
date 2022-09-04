import json
from random import choice

def gen_person():
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7']

    while len(name) != 5:
        name += choice(letters)
    while len(tel) != 9:
        tel += choice(nums)

    person = {
        'name': name,
        'tel': tel,
    }
    return person

def write_json(person_dict):
    try:
        data = json.load(open('test.json'))
    except:
        data = []
    data.append(person_dict)

    with open('test.json', 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def main():

    persons = []

    for i in range(1):
        write_json(gen_person())


if __name__ == '__main__':
    main()