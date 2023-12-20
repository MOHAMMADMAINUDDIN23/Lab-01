def fibonacci(n):
    fib_sequence = [0, 1]
    fib_sequence.extend(fib_sequence[i-1] + fib_sequence[i-2] for i in range(2, n))
    return fib_sequence

x = int(input("Enter the number of terms: "))
print(f"Fibonacci sequence of {x} terms: {fibonacci(x)}")