import sys
from collections import defaultdict
from math import isqrt


def sieve_smallest_prime(limit):
    spf = list(range(limit + 1))
    for i in range(2, isqrt(limit) + 1):
        if spf[i] == i:
            for j in range(i * i, limit + 1, i):
                if spf[j] == j:
                    spf[j] = i
    return spf


def prime_factors(x, spf):
    factors = defaultdict(int)
    while x != 1:
        factors[spf[x]] += 1
        x //= spf[x]
    return factors


def compute_prefix_factors(A, spf):
    n = len(A)
    prefix_factors = [defaultdict(int) for _ in range(n + 1)]

    for i in range(1, n + 1):
        factors = prime_factors(A[i - 1], spf)
        prefix_factors[i] = prefix_factors[i - 1].copy()
        for p, count in factors.items():
            prefix_factors[i][p] += count

    return prefix_factors


def calculate_game_result(L, R, prefix_factors):
    factor_counts = defaultdict(int)

    for p, count in prefix_factors[R].items():
        factor_counts[p] += count
    for p, count in prefix_factors[L - 1].items():
        factor_counts[p] -= count

    xor_sum = 0
    for count in factor_counts.values():
        xor_sum ^= count

    return "COUSIN" if xor_sum == 0 else "IGNACIO"


def solve():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    max_val = 10**7
    spf = sieve_smallest_prime(max_val)

    prefix_factors = compute_prefix_factors(A, spf)

    for _ in range(M):
        L, R = map(int, input().split())
        print(calculate_game_result(L, R, prefix_factors))


if __name__ == "__main__":
    solve()


"""
Run Time Error
"""
