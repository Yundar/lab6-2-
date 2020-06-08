from functions import *
from classes import *
# 1002 231 435 457 23 654 234 567 3578 3498702
dollars = list(input('Введите количество USD в кассе через пробел\n'
                     '(1-е число - 1000, 2-е - 500... 10-e - 1): ').split())

uah = list(input('Введите количество UAH в кассе через пробел\n'
                 '(1-е число - 1000, 2-е - 500... 10-e - 1): ').split())

dollars = make_dict(dollars)
uah = make_dict(uah)
print(dollars)
cash = Cashbox(dollars, uah)
cash.check_dollars(22311)