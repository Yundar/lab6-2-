import datetime
import copy

today = datetime.datetime.today()
print(today.strftime("%Y-%m-%d %H:%M:%S"))


class Cashbox:
    def __init__(self, dollars, uah):
        self.dollars = dollars
        self.uah = uah
        self.dollars_uah = 26.58
        self.uah_dollars = 0.038

    def check_dollars(self, sum, currency):
        l = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
        f = []
        for i in range(2, len(str(sum)) + 1):
            c = copy.deepcopy(sum)
            f.append(c * 10 ** (-len(str(sum)) + i))
        quantity = [0 for i in range(len(l))]
        print(f)

        for i in range(-1, -len(f), -1):
            c = 1
            if i != 0:
                f[i] = f[i] - int(f[i - 1]) * 10 ** c
            c += 1
        for i in range(len(f)):
            f[i] = int(f[i])
        j = 0
        for i in range(0, len(quantity), 3):
            quantity[i] = f[j]
            j += 1
        
        print(quantity)
