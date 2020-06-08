def make_dict(list):
    dl = dict()
    for i in range(len(list)):
        list[i] = int(list[i])
    for i in range(1, len(list), 2):
        dl[list[i-1]] = list[i]
    return dl