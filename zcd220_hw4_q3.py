# 3a

def print_triangle(n):
    if n == 0:
        return None
    print_triangle(n - 1)
    for i in range(n):
        print("*", end="")
    print()


# 3b

def print_opposite_triangles(n):
    if n == 0:
        return
    for i in range(n):
        print("*", end="")
    print()
    print_opposite_triangles(n - 1)
    for i in range(n):
        print("*", end="")
    print()


# 3c

def print_ruler(n):
    if n == 0:
        return
    print_ruler(n - 1)
    for i in range(n):
        print("-", end="")
    print()
    print_ruler(n - 1)
