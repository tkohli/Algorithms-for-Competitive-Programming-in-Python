"""
Binary exponentiation (also known as exponentiation by squaring) is a trick which allows to 
calculate a^n using only O(log n) multiplications (instead of O(n) multiplications required 
by the naive approach).

https://cp-algorithms.com/algebra/binary-exp.html#applying-a-permutation-k-times

Algo:
    a^n
if n==0:        return 1
if n is even:   (a^(n/2))^2
if n is odd:    (a^(n-1/2))^2

"""
# recursion
def binpow(a, n):
    if n == 0:
        return 1
    res = binpow(a, n // 2)
    if n % 2: # odd
        return res * res * a
    else: # even
        return res * res

# print(binpow(3,13))

#bit manupulation
def binpowBit(a, n):
    res= 1
    while n > 0:
        if n & 1: # x & 1 produces a value that is either 1 or 0, depending on the least significant bit of x
            res = res * a
        a = a * a
        n >>= 1 # x >>= 1 means "set x to itself shifted by one bit to the right"
    return res


print(binpowBit(3,13))