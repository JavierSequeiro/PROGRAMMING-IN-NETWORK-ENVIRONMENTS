x = 0
y = 1
fibonacci_list = [x, y]
limit = 11
for i in range (0, limit - 2):
    fn = x + y
    fibonacci_list.append(fn)
    x = y
    y = fn
#print(fibonacci_list)
for i in fibonacci_list:
    print(i, end= " ")