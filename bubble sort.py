def bubbleSort(numlist):
    for x in range(len(numlist)-1,0,-1):
        for i in range(x):
            if numlist[i]>numlist[i+1]:
                temp = numlist[i]
                numlist[i] = numlist[i+1]
                numlist[i+1] = temp

numlist= [34,46,3,1,45,78,97,43]

bubbleSort(numlist)
print(numlist)
