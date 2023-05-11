# Primality tests
# 1st naive way to check all val looping - Trial division

# Fermat primality test
"""
Note bad for large prime number
for 1<=a<p if (a^p)-a is multiple of p then is is a prime number

There is one bad news though: there exist some composite numbers where a^{n-1} =1%n
holds for all a coprime to n, for instance for the number 
561 = 3 * 11 * 17. Such numbers are called Carmichael numbers. 
"""

# Miller-Rabin primality test
"""
Miller-Rabin is a probabilistic primality testing algorithm that is used to check if a given number is prime or composite. It is based on the observation that if n is a composite number, then it must have a factor less than or equal to sqrt(n). The algorithm randomly selects several numbers and checks whether they are witnesses to n's compositeness. If a number a is a witness to n's compositeness, then it means that n is definitely composite.

Here's an example: Let's say we want to check if the number 91 is prime. We randomly choose the number 2 as our first witness. We then compute the value of 2^(n-1) modulo n, which is (2^90) modulo 91. If this value is not equal to 1, then we know that 2 is a witness to 91's compositeness. We then choose another random number, say 7, and compute the value of 7^(n-1) modulo n, which is (7^90) modulo 91. If this value is also not equal to 1, then we know that 7 is also a witness to 91's compositeness. In this case, 91 is composite, as it has two witnesses to its compositeness (2 and 7).
"""
from typing import Tuple
import random
import math

u64 = int
u128 = int

def binpower(base: u64, e: u64, mod: u64) -> u64:
    result = 1
    base %= mod
    while e:
        if e & 1:
            result = (u128(result) * base) % mod
        base = (u128(base) * base) % mod
        e >>= 1
    return result

def check_composite(n: u64, a: u64, d: u64, s: int) -> bool:
    x = binpower(a, d, n)
    if x == 1 or x == n - 1:
        return False
    for r in range(1, s):
        x = (u128(x) * x) % n
        if x == n - 1:
            return False
    return True

def MillerRabin(n: u64, iter: int = 5) -> bool:
    if n < 4:
        return n == 2 or n == 3

    s = 0
    d = n - 1
    while (d & 1) == 0:
        d >>= 1
        s += 1

    for i in range(iter):
        a = random.randint(2, n - 2)
        if check_composite(n, a, d, s):
            return False
    return True


print(MillerRabin(53))