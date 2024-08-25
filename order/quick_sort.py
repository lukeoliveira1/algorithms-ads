import random
import time

# O (log n)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)



if __name__ == "__main__":

    total = 1000000
    while total > 1:
        begin = time.time()

        arr = random.sample(range(10000000), k=total)
        arr2 = random.choices(range(100), k=total)
        # sample create array without repeat numbers
        # choices create array with repeat numbers

        quick_sort(arr)

        end = time.time()

        print(total, " - ", end - begin, "s \n")

        total = int(total / 2)