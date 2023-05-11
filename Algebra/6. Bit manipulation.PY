# Bit manipulation
"""
CPUs are very fast manipulating those bits with specific operations. For some problems we can take these binary number representations to our advantage, and speed up the execution time. 

Bitwise operators

& : The bitwise AND operator compares each bit of its first operand with the corresponding bit of its second operand. If both bits are 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.

| : The bitwise inclusive OR operator compares each bit of its first operand with the corresponding bit of its second operand. If one of the two bits is 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.

^ : The bitwise exclusive OR (XOR) operator compares each bit of its first operand with the corresponding bit of its second operand. If one bit is 0 and the other bit is 1, the corresponding result bit is set to 1. Otherwise, the corresponding result bit is set to 0.

~ : The bitwise complement (NOT) operator flips each bit of a number, if a bit is set the operator will clear it, if it is cleared the operator sets it.

Examples:

n         = 01011000
n-1       = 01010111
--------------------
n & (n-1) = 01010000

n         = 01011000
n-1       = 01010111
--------------------
n | (n-1) = 01011111

n         = 01011000
n-1       = 01010111
--------------------
n ^ (n-1) = 00001111

n         = 01011000
--------------------
~n        = 10100111


Shift operators
There are two operators for shifting bits.
>> right shift
<< left shift

# still todo https://cp-algorithms.com/algebra/bit-manipulation.html#shift-operators
"""