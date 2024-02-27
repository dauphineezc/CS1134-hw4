def appearances(s, low, high):
    if low > high or s == "":
        return {}
    if low == high:
        return {s[low]: 1}
    dictionary = appearances(s, low + 1, high)
    if s[low] in dictionary:
        dictionary[s[low]] += 1
    else:
        dictionary[s[low]] = 1
    return dictionary


