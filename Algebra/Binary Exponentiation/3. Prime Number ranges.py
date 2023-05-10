# Find primes in range
# Segmented Sieve
import math

def count_primes(n):
    S = 10000

    primes = []
    nsqrt = int(math.sqrt(n))
    is_prime = [True] * (nsqrt + 2)
    for i in range(2, nsqrt + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, nsqrt + 1, i):
                is_prime[j] = False

    result = 0
    block = [True] * S
    for k in range((n + S - 1) // S):
        block = [True] * S
        start = k * S
        for p in primes:
            start_idx = (start + p - 1) // p
            j = max(start_idx, p) * p - start
            while j < S:
                block[j] = False
                j += p
        if k == 0:
            block[0] = block[1] = False
        for i in range(S):
            if start + i > n:
                break
            if block[i]:
                result += 1
                print(i)
    return result

# ______________________
# Linear Sieve
N = 10000000
lp = [0]*(N+1)
prime = []

"""
if lp[i] == 0 that means i is prime, add lp[i]=i and append to prime
else add its minimum prime factor is lp[i].
"""
for i in range(2,N+1):
    if lp[i] == 0:
        lp[i] = i
        prime.append(i)
    j = 0
    while i * prime[j] <= N:
        lp[i * prime[j]] = prime[j]
        if prime[j] == lp[i]:
            break
        j += 1
print(prime)

# print(count_primes(100))