import random
n = [x for x in range(1,21)]
random.shuffle(n)
print(n)

for i in range(len(n)-1,0,-1):
    for j in range(len(n)):
        if (i + j < len(n)):
            if(n[i+j] < n[j]):
                n[i+j], n[j] = n[j], n[i+j]
        else:
            break

print(n)