def make_dict(list):
    dl = dict()
    l = [1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
    for i in range(len(list)):
        list[i] = int(list[i])
    for i in range(len(list)):
        dl[l[i]] = list[i]
    return dl
