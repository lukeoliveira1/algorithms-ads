def read_two_arrays():
    import random

    a = []
    b = []

    for i in range(20):
        a.append(random.randint(15, 30))
        b.append(random.randint(1, 10))

    print(a)
    print(b)

    c = []
    d = []
    e = []

    for x, j in zip(a, b):
        c.append(x-j)
        d.append(x+j)
        e.append(x*j)

    print(c)
    print(d)
    print(e)

########################################
import random

a = []

for i in range(10):
    a.append(random.randint(1, 30))

print("antes")
print(a)

#dividir e conquistar, é um MergeSort
def mergeSort(arr):
    #dividir
    if len(arr)>1:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        #conquistar
        i=0
        j=0
        k=0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k]=left[i]
                i=i+1
            else:
                arr[k]=right[j]
                j=j+1
            k=k+1

        while i < len(left):
            arr[k]=left[i]
            i=i+1
            k=k+1

        while j < len(right):
            arr[k]=right[j]
            j=j+1
            k=k+1

# print("depois")
# mergeSort(a)
# print(a)

def mergeSortTwo(arr):
    if (len(arr)>1):
        mid = len(arr)//2;
        left = arr[:mid]
        right = arr[mid:]

        mergeSort(left)
        mergeSort(right)

        i, j, k = 0, 0, 0

        while(i < len(left) and j < len(right)):
            if i <= j:
                arr[k] = left[i];
                i += 1;
            else:
                arr[k] = left[j];
                j += 1
            k += 1
        
        while(i < len(left)):
            arr[k] = left[i];
            i += 1;
            k += 1; 

        while(j < len(left)):
            arr[k] = left[j];
            j += 1;
            k += 1; 
        
print("depois")
mergeSortTwo(a)
print(a)