def solve():
    T = int(input())

    for _ in range(T):
        N = int(input())

        if N == 0:
            print("haha good one")
        elif N >= 180:
            print("canceled")
        else:
            berkeley_count = N // 10
            print("berkeley" * berkeley_count + "time")


solve()
