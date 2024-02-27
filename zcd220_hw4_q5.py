# 5a

def count_lowercase(s, low, high):
    if low == high and s[low] == s[low].lower():
        return 1
    elif low == high and s[low] != s[low].lower():
        return 0
    elif s[low] == s[low].lower():
        return 1 + count_lowercase(s, low + 1, high)
    elif s[low] != s[low].lower():
        return count_lowercase(s, low + 1, high)


# 5b

def is_number_of_lowercase_even(s, low, high):
    if low > high:
        return True
    elif s[low].islower():
        return not is_number_of_lowercase_even(s, low+1, high)
    else:
        return is_number_of_lowercase_even(s, low+1, high)
