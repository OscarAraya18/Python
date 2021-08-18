def quickSort(arrayToSort):
    auxiliarQuickSort(arrayToSort, 0, len(arrayToSort)-1)

def auxiliarQuickSort(arrayToSort, startingIndex, endingIndex):
    if len(arrayToSort) == 1:
        return arrayToSort

    if(startingIndex < endingIndex):
        partitionIndex = partition(arrayToSort, startingIndex, endingIndex)

        auxiliarQuickSort(arrayToSort, startingIndex, partitionIndex-1)
        auxiliarQuickSort(arrayToSort, partitionIndex+1, endingIndex)

def partition(arrayToSort, startingIndex, endingIndex):
    i = startingIndex-1
    pivot = arrayToSort[endingIndex]

    for j in range(startingIndex,endingIndex):
        if arrayToSort[j] <= pivot:
            i += 1
            arrayToSort[i], arrayToSort[j] = arrayToSort[j], arrayToSort[i]

    arrayToSort[i+1], arrayToSort[endingIndex] = arrayToSort[endingIndex], arrayToSort[i+1]
    return i + 1


array = [-2,-10,11,0]
quickSort(array)
print(array)