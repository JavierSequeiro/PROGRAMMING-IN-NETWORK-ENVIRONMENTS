def fibon(n):
    x = 0
    y = 1
    fibonacci_list = [x, y]
    for i in range(0, n - 1):
        fn = x + y
        fibonacci_list.append(fn)
        x = y
        y = fn
    return fibonacci_list[-1]

print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))