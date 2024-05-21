import numpy as np
import time

# bubble-sort compares one item with the next item and changes its position if the next one is higher

total = 10000
arr = np.random.randint(1, 100, size=total)


def bubble_sort(array):
    for num in range(len(array) - 1, 0, -1):
        for i in range(num):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp


begin = time.time()
bubble_sort(arr)
end = time.time()
print(total, " - ", end - begin, "s \n")
