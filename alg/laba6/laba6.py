import random
n = [x for x in range(1,5)]
random.shuffle(n)
print(n)

ind = 0
for i in range(len(n)-1):
    minim = n[i+1]
    for j in range(i+1, len(n)):
        if n[j] < minim:
            minim = n[j]
            ind = j
    if n[i] > minim:
        n[i], n[ind] = n[ind], n[i]

print(n)
