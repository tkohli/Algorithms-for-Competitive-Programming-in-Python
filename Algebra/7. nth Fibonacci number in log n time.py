# nth Fibonacci number
def matrix_multiply(a, b):
    # Helper function to multiply two matrices
    return [[sum(a[i][k]*b[k][j] for k in range(len(a[0]))) for j in range(len(b[0]))] for i in range(len(a))]

def matrix_power(m, n):
    # Compute the nth power of a matrix using binary exponentiation
    result = [[1, 0], [0, 1]]  # Identity matrix
    while n > 0:
        if n % 2 == 1:
            result = matrix_multiply(result, m)
        m = matrix_multiply(m, m)
        n //= 2
    return result

def fibonacci(n):
    # Compute the nth Fibonacci number using the matrix method
    if n == 0:
        return 0
    m = [[1, 1], [1, 0]]
    return matrix_power(m, n-1)[0][0]

# Test the implementation
# print(fibonacci(0))  # 0
# print(fibonacci(1))  # 1
# print(fibonacci(2))  # 1
# print(fibonacci(3))  # 2
# print(fibonacci(4))  # 3
# print(fibonacci(5))  # 5
# print(fibonacci(6))  # 8

# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         for i in range(2,n+1):
#             c = a + b
#             a = b
#             b = c
#         return b
 
# Driver Program
 
# print(fibonacci(9))
print(fibonacci(700000))  # 13
