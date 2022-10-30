import json

def load_json(filename):
    with open(filename, encoding="utf-8") as infile:
        return json.load(infile)


def write_json(filename, content):
    with open(filename, "w", encoding="utf-8") as outfile:
        json.dump(content, outfile, ensure_ascii=False, indent=4)


users = load_json('data/jsons/users.json')
teacher = load_json('data/jsons/teachers.json')

lessons_default = load_json('data/jsons/lessons.json')
lessons_first = load_json('data/jsons/lessons_first.json')

calls_json = load_json('data/jsons/calls.json')

def get_teacher(subject, num):
    return f'''
{subject}

ФИО: {teacher[str(subject)][num]["ФИО"]}
Номер телефона: {teacher[str(subject)][num]["Номер телефона"]}
email: {teacher[str(subject)][num]["email"]}
VK: {teacher[str(subject)][num]["VK"]}
Сайт: {teacher[str(subject)][num]["link"]}
    '''

def get_day_default(week_num, day):
    for t in lessons_default[str(week_num)]:
        res = t[str(day)]
    return ''.join(res)

def get_day_first(week_num, day):
    for t in lessons_first[str(week_num)]:
        res = t[str(day)]
    return ''.join(res)