from datetime import date as dt
from datetime import time as tm
from func import *
# from main import *

lessons = load_json('jsons/lessons.json')

mon = 0; tue = 1; wed = 2; thu = 3; fri = 4; sat = 5; sun = 6

def get_day(week_num, day):
    for t in lessons[str(week_num)]:
        res = t[str(day)]
    return ''.join(res)

ch = "четная"
nch = "нечетная"

full_1 = \
    "Расписание четной недели: \n\n" + \
    get_day(ch, 0) + "\n\n" + \
    get_day(ch, 1) + "\n\n" + \
    get_day(ch, 2) + "\n\n" + \
    get_day(ch, 3) + "\n\n" + \
    get_day(ch, 4) + "\n\n"

full_2 = \
    "Расписание нечетной недели: \n\n" + \
    get_day(nch, 0) + "\n\n" + \
    get_day(nch, 1) + "\n\n" + \
    get_day(nch, 2) + "\n\n" + \
    get_day(nch, 3) + "\n\n" + \
    get_day(nch, 4) + "\n\n"