def fibonacci_sequence(n):
    fib = [0, 1]
    [fib.append(fib[-1] + fib[-2]) for _ in range(2, n)]
    return fib[:n]

n = int(input("Enter the value of n: "))
sequence = fibonacci_sequence(n)
print(','.join(map(str, sequence)))