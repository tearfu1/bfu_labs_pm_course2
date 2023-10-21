def putInTable(myhash, value, table, step=1):
    for i in range(myhash, len(table)*(step != -1), step):
        if table[i] == 0:
            table[i] = value
            return True
        #if table[i] == value: #могут ли значения в таблице повторяться?
            # return True
    return False
with open("example.txt") as file:
    text = file.read()

words = text.split()
table = [0]*31

for i in words:
    temp_sum = 0
    for j in i:
        if j in "!.,?';":
            myhash = ord(j) % len(table)
            if not putInTable(myhash, j, table):
                putInTable(myhash, j, table, -1)
            i = i[:len(i)-1]
        temp_sum += ord(j)
    myhash = temp_sum % len(table)
    if not putInTable(myhash, i, table):
        putInTable(myhash, i, table, -1)

with open("table.txt","w") as file:
    for i in range(len(table)):
        temp_string = f"{i} : {table[i]}\n"
        file.write(temp_string)