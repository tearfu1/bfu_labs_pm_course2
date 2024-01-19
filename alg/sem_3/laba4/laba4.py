import random
n = [x for x in range(1,21)]
random.shuffle(n)
print(n)

size = len(n)
step = size
flag = False

while flag or step>1:
    if step>1:
        step = int(step/1.247)
    
    flag, i = False, 0
    while i+step<size:
        if n[i] > n[i+step]:
            n[i], n[i+step] = n[i+step],n[i]
            flag = True
        i+=step
print(n)
