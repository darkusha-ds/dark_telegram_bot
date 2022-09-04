from calendar import week
import datetime, json

with open('lessons.json', 'r') as f:
    lessons = json.load(f)

x = input("Day: ")

today = datetime.datetime.today().weekday()
week_now = datetime.datetime.today().isocalendar().week
tomorrow = today + 3
yesterday = today - 4

if tomorrow >= 7: 
    tomorrow = 0
    week_now = week_now + 1
if yesterday < 0: yesterday = 0

def get_day(week_num, day):
    for t in lessons[str(week_num)]:
        res = t[str(day)]
    return ''.join(res)

def get_call():
    res = lessons["звонки"]
    print(''.join(res))

def less_today():
    if week_now % 2 == 0: print(get_day("четная", today))
    else: print(get_day("нечетная", today))

def less_tomor():
    if week_now % 2 == 0: print(get_day("четная", tomorrow))
    else:  print(get_day("нечетная", tomorrow))

def less_yest():
    if week_now % 2 == 0: print(get_day("четная", yesterday))
    else: print(get_day("нечетная", yesterday))

if x == "1": less_today()
elif x == "2": less_tomor()
elif x == "3": less_yest()
elif x == "4": get_call()

# print(output)