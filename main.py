import random
import time


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Test insertion sort and merge sort for different values of n
for n in range(0, 100):  # [20, 25, 30, 35, 40, 45, 50]:
    arr = [random.randint(1, 100) for _ in range(n)]

    start_time = time.time()
    it = 0
    while it != 1000:
        insertion_sort(arr.copy())
        it += 1
    insertion_time = time.time() - start_time

    start_time = time.time()
    it = 0
    while it != 1000:
        merge_sort(arr.copy())
        it += 1
    merge_time = time.time() - start_time

    print(f"n = {n}: Insertion sort took {insertion_time:.6f} seconds, Merge sort took {merge_time:.6f} seconds")