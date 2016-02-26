import random
def insertionSort(randomItems):
   
    for i in range(1, len(randomItems)):
        j = i
        while j > 0 and randomItems[j] < randomItems[j-1]:
            randomItems[j], randomItems[j-1] = randomItems[j-1], randomItems[j]
            j -= 1

randomItems = [random.randint(-50, 100) for c in range(10)]
print(randomItems)
insertionSort(randomItems)
print(randomItems)            
