import random
ls = [i+random.randint(1,1001) for i in range(1, 21)]
random.shuffle(ls)
print(ls)

n = len(ls)
maxim = -10

for i in ls:
    maxim = max(i, maxim)

ranks = 0
while maxim > 0:
    maxim //= 10
    ranks += 1

for i in range(ranks):
    digits = [[], [], [], [], [], [], [], [], [], []]
    int_part = 10**(i+1)
    rem_part = 10**i
    for j in range(len(ls)):
        temp_int = ls[j] % int_part
        curr_rank = temp_int // rem_part
        digits[curr_rank].append(ls[j])
    ls = [x for queue in digits for x in queue]

print(ls)
