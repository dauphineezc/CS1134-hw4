def permutations(lst, low, high):
    if low == high:
        return [lst[low: high + 1]]
    permutations_lst = []
    for i in range(low, high + 1):
        lst[low], lst[i] = lst[i], lst[low]
        sub_permutations = permutations(lst, low + 1, high)
        for elem in sub_permutations:
            permutations_lst.append([lst[low]] + elem)
        lst[low], lst[i] = lst[i], lst[low]
    return permutations_lst
