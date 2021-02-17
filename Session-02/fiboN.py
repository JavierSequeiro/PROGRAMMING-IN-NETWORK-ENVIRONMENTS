def fibon(n):
    x = 1
    y = 1
    for i in range(0, n - 2):
        fn = x + y
        x = y
        y = fn
    return fn

print("5th Fibonacci term: ", fibon(5))
print("10th Fibonacci term: ", fibon(10))
print("15th Fibonacci term: ", fibon(15))