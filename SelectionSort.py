def selectionSort(arrayToSort):
    for i in range(len(arrayToSort)):
        minimumIndex = i

        for j in range(i+1, len(arrayToSort)):
            if arrayToSort[minimumIndex] > arrayToSort[j]:
                minimumIndex = j

        arrayToSort[i], arrayToSort[minimumIndex] = arrayToSort[minimumIndex], arrayToSort[i]


array = [20,-6,10,2,0,1,44,0]
selectionSort(array)
print(array)