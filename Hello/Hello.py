addition = 0
for n in range (1, 21):
    addition += n

print(addition)

def sum(n):
    summatory = 0
    for i in range (1, n + 1):
        summatory += i
    return summatory

#number = int(input("Enter the last element of the sum: "))
print(f"The sum of the first {20} numbers  is ", sum(20))

