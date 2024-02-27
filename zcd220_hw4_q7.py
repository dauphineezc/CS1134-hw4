def split_by_sign(lst, low, high):
    if low >= high:
        return lst
    while low <= high and lst[low] < 0:
        low += 1
    while high >= low and lst[high] > 0:
        high -= 1
    if low < high:
        lst[low], lst[high] = lst[high], lst[low]
        split_by_sign(lst, low+1, high-1)
