import random


def heapsort(array):
    buildMaxHeap(array)
    n = len(array)
    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        n -= 1
        heapify(array, 0, n)


def buildMaxHeap(array):
    n = len(array)
    for i in range(n//2, -1, -1):
        heapify(array, i, n)


def heapify(array, i, array_size):
    left = 2*i+1
    right = 2*i+2
    n = array_size
    maxim = i

    if left < n and array[left] > array[i]:
        maxim = left

    if right < n and array[right] > array[maxim]:
        maxim = right

    if maxim != i:
        array[maxim], array[i] = array[i], array[maxim]
        heapify(array, maxim, n)


ls = [i+random.randint(1,1001) for i in range(1, 21)]
random.shuffle(ls)
print(ls)
heapsort(ls)#nlogn
print(ls)
