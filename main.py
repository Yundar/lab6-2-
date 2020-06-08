from functions import *

dollars = list(input('Введите количество USD в кассе через пробел\n'
                     '(1-е число - купюра, 2-е - количество): ').split())
eur = list(input('Введите количество EUR в кассе через пробел\n'
                     '(1-е число - купюра, 2-е - количество): ').split())
uah = list(input('Введите количество UAH в кассе через пробел\n'
                     '(1-е число - купюра, 2-е - количество): ').split())
dollars = make_dict(dollars)
eur = make_dict(eur)
uah = make_dict(uah)
