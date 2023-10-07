import random
import time

# divide and conquer is merge sort!
# merge-sort splits the array into smaller arrays, sorts them separately and merges them later


def merge_sort(array):
    # divide
    if len(array) > 1:
        mid = len(array) // 2
        left = array[:mid]
        right = array[mid:]

        merge_sort(left)
        merge_sort(right)

        # conquer
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


if __name__ == "__main__":

    total = 1000000
    while total > 1:
        begin = time.time()

        arr = random.sample(range(10000000), k=total)
        arr2 = random.choices(range(100), k=total)
        # sample create array without repeat numbers
        # choices create array with repeat numbers

        merge_sort(arr)

        end = time.time()

        print(total, " - ", end - begin, "s \n")

        total = int(total / 2)
