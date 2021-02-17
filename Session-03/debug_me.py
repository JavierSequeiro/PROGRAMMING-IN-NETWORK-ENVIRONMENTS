def g(a, b):
    return a - b


def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    if c != d:
        t3 = 2 * (t0 / t1)
        return t0 + 2*t1 + t3*t3
    else:
        return "You must input a c value different from d."


# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))

#c and d must be different from 0 since we need t1 != 0