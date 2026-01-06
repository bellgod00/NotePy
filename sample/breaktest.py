for n in range(2, 10):
    print(f"n-->{n}")
    for x in range(2, n):
        print(f"x==>{x}")
        if n % x == 0:
            print(f"{n} equals {x} * {n//x}")
            break