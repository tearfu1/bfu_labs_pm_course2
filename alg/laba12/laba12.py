from laba11 import quicksort


def finalwrite (i, array):
    with open(f"ans{i}.txt", "w") as f:
        temp_s = ' '.join(map(str, array))
        f.write(temp_s)


i = 0
while True:
    try:
        with open(f'example{i}.txt') as file:
            array = list(map(int, file.read().split()))
            quicksort(array,0,len(array)-1)
            #print(array)
        with open(f"temp{i}.txt", "w") as file:
            temp_str = ' '.join(map(str, array))
            file.write(temp_str)
    except FileNotFoundError:
        break
    i += 1


min_file_ind = 0
ans_file_cnt = 0
temp_ans_array = []
while True:
    temp_file_array = []
    flag = False
    minim = 99999999999
    for j in range(i):
        with open(f"temp{j}.txt") as file:
            array = list(map(int, file.read().split()))
            if len(array) != 0:
                flag = True
                if array[0] < minim:
                    minim = min(array[0], minim)
                    min_file_ind = j
                    temp_file_array = array
                    del(temp_file_array[0])

    if not flag:
        finalwrite(ans_file_cnt, temp_ans_array)
        break

    with open(f"temp{min_file_ind}.txt", "w") as file:
        temp_str = ' '.join(map(str, temp_file_array))
        file.write(temp_str)

    if len(temp_ans_array) < 10:
        temp_ans_array.append(minim)
    else:
        finalwrite(ans_file_cnt, temp_ans_array)
        ans_file_cnt += 1
        temp_ans_array.clear()
        temp_ans_array.append(minim)
