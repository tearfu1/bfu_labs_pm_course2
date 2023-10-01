import random


def merge(array1, array2):
    sortedList = []
    while len(array1) != 0 and len(array2) != 0:
        if array1[0] < array2[0]:
            sortedList.append(array1[0])
            del(array1[0])
        else:
            sortedList.append(array2[0])
            del (array2[0])
    sortedList += array1
    sortedList += array2
    return sortedList


def mergesort(array):
    if len(array) == 1:
        return array
    n = len(array)
    leftHalf = array[:n//2]
    rightHalf = array[n//2:]
    sortedLeftHalf = mergesort(leftHalf)
    sortedRightHalf = mergesort(rightHalf)
    sortedList = merge(sortedLeftHalf, sortedRightHalf)
    return sortedList


ls = [i+random.randint(1,1001) for i in range(1, 22)]
random.shuffle(ls)
print(ls)
ls = mergesort(ls)#nlogn
print(ls)
