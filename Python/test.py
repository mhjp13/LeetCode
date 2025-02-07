def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# Example usage:
n = 10
print(f"First {n} Fibonacci numbers: {fibonacci(n)}")
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Example usage:
n = 5
print(f"Factorial of {n}: {factorial(n)}")

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Example usage:
num = 29
print(f"Is {num} a prime number? {is_prime(num)}")