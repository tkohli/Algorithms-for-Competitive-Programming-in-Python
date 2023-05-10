# Integer factorization

def trial_division1(n):
    factorization = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factorization.append(d)
            n //= d
        d += 1
    if n > 1:
        factorization.append(n)
    return factorization

print(trial_division1(100))

# optimization could be Precomputed primes, i like doing this 
# https://cp-algorithms.com/algebra/factorization.html#pollards-rho-algorithm
# Brent's algorithm
"""
"""
def f(x, c, n):
    return (x * x + c) % n

def mult(a, b, n):
    return (a * b) % n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def brent(n, x0=2, c=1):
    x, g, q, xs, y = x0, 1, 1, 0, 0
    m, l = 128, 1

    while g == 1:
        y = x
        for i in range(1, l):
            x = f(x, c, n)
        k = 0
        while k < l and g == 1:
            xs = x
            for i in range(min(m, l - k)):
                x = f(x, c, n)
                q = mult(q, abs(y - x), n)
            g = gcd(q, n)
            k += m
        l *= 2

    if g == n:
        while g == n:
            xs = f(xs, c, n)
            g = gcd(abs(xs - y), n)
    return g


print(brent(100))