import random
n = [x for x in range(1,21)]
random.shuffle(n)
print(n)

for i in range(1, len(n)):
    for j in range(i,0,-1):
        if n[j] < n[j-1]:
            n[j], n[j-1] = n[j-1], n[j]
        else:
            break

print(n)
