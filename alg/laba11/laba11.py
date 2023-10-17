import random


def partition(array, low, high):
    pivot = array[high]
    left = low

    for i in range(low, high):
        if array[i] <= pivot:
            array[i], array[left] = array[left], array[i]
            left += 1
    array[high], array[left] = array[left], array[high]

    return left


def quicksort(array, low, high):
    if low < high:
        pivot_location = partition(array, low, high)
        quicksort(array, low, pivot_location - 1)
        quicksort(array, pivot_location + 1, high)


ls = [i+random.randint(1,1001) for i in range(1, 21)]
#ls = [x for x in range(20)]
random.shuffle(ls)
print(ls)
quicksort(ls, 0, len(ls)-1)  #nlogn
print(ls)
