import random
ls = [x for x in range(1,21)]
random.shuffle(ls)
print(ls)

n = len(ls)
step = n//2

while step > 0:
    for i in range(step, n): #n(logn)^2
        j = i
        d = j-step
        while d >= 0 and ls[d] > ls[j]:
            ls[d], ls[j] = ls[j], ls[d]
            j = d
            d = j - step
    step //= 2

print(ls)
