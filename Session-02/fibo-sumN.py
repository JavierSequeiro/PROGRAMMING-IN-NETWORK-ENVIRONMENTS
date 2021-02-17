def fibosum(n):
    x = 0
    y = 1
    fibonacci_list = [x, y]
    for i in range(0, n - 1):
        fn = x + y
        fibonacci_list.append(fn)
        x = y
        y = fn
    return fibonacci_list

print("Sum of the first 5 Fibonacci series: ", sum(fibosum(5)))
print("Sum of the first 10 Fibonacci series: ", sum(fibosum(10)))