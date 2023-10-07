# get the largest number in the array with merge-sort
# do mergeSort and return the last position
import random
import time


def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array[k] = left[i]
                i = i + 1
            else:
                array[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            array[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            array[k] = right[j]
            j = j + 1
            k = k + 1

        return array[k - 1]


if __name__ == "__main__":
    total = 10000000

    begin = time.time()

    arr = random.choices(range(5000000), k=total)

    print(merge_sort(arr))

    end = time.time()

    print("with ", total, " elements - ", end - begin, "s \n")
