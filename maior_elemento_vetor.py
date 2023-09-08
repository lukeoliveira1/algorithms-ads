import random
import time 

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
    
        i, j, k = 0 , 0, 0
        
        while(i < len(left) and j < len(right)):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        
        while i < len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j < len(right):
            arr[k] = right[j]
            j+=1
            k+=1

        return arr[k-1]

inicio = time.time()

arr = random.choices(range(999999),  k=10000000)
print(merge_sort(arr))

fim = time.time()

print("com 1.000.000 elementos - ", fim - inicio, "s \n")

