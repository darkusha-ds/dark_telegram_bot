from datetime import date as dt
from datetime import time as tm
from func import *

data = load_json('jsons/lessons.json')

mon = 0; tue = 1; wed = 2; thu = 3; fri = 4; sat = 5; sun = 6

def less(cls_num, day):
    for t in data[str(cls_num)]:
        res = t[str(day)]
    return ''.join(res)

adm10 = less(10, 0)+'\n\n'+less(10, 1)+'\n\n'+less(10, 2)+'\n\n'+less(10, 3)+'\n\n'+less(10, 4)+'\n\n'+less(10, 5)+'\n\n'+less(10, 6)
adm11 = less(11, 0)+'\n\n'+less(11, 1)+'\n\n'+less(11, 2)+'\n\n'+less(11, 3)+'\n\n'+less(11, 4)+'\n\n'+less(11, 5)+'\n\n'+less(11, 6)