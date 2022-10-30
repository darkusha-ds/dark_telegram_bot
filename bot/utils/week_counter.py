from utils.func import *
from utils.phrazes import *

even_week = f'''
Расписание четной недели:

{get_day_default(even_wk, 0)}
{get_day_default(even_wk, 1)}
{get_day_default(even_wk, 2)}
{get_day_default(even_wk, 3)}
{get_day_default(even_wk, 4)}
'''

odd_week = f'''
Расписание нечетной недели:

{get_day_default(odd_wk, 0)}
{get_day_default(odd_wk, 1)}
{get_day_default(odd_wk, 2)}
{get_day_default(odd_wk, 3)}
{get_day_default(odd_wk, 4)}
'''