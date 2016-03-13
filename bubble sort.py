import random
def bubbleSort(randomItems):
    for x in range(len(randomItems)-1,0,-1):
        for i in range(x):
            if randomItems[i]>randomItems[i+1]:
                temp = randomItems[i]
                randomItems[i] = randomItems[i+1]
                randomItems[i+1] = temp


randomItems = [random.randint(-50, 100) for c in range(10)]
print(randomItems)
bubbleSort(randomItems)
print(randomItems)
