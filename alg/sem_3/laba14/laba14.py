def putInTable(myhash, value, table):
    table[myhash].append(value)

with open("example.txt") as file:
    text = file.read()

words = text.split()
table = []
for i in range(len(words)*2):
    table.append([])
for i in words:
    temp_sum = 0
    for j in i:
        if j in "!.,?';":
            myhash = ord(j) % len(table)
            putInTable(myhash, j, table)
            i = i[:len(i)-1]
        temp_sum += ord(j)
    myhash = temp_sum % len(table)
    putInTable(myhash, i, table)

with open("table.txt","w") as file:
    for i in range(len(table)):
        temp_string = f"{i} : {table[i]}\n"
        file.write(temp_string)
