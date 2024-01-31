def swapList(sl, pos1, pos2):
    sl[pos1], sl[pos2] = sl[pos2], sl[pos1]
    return sl


List = [9, 11, 5, 3, 6, 27, 4]
pos1, pos2 = 3, 5
print(List)
print("Swapped List: ", swapList(List, pos1 - 1, pos2 - 1))