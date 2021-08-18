def insertionSort(arrayToSort):
    for i in range(1,len(arrayToSort)):
        currentElement = arrayToSort[i]

        j = i-1
        while j >= 0 and currentElement < arrayToSort[j]:
            arrayToSort[j+1] = arrayToSort[j]
            j -= 1
        arrayToSort[j+1] = currentElement


array = [20,-6,10,2,0,1,44,0]
insertionSort(array)
print(array)