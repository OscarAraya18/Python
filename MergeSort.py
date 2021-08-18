
def mergeSort(arrayToSort):

    if len(arrayToSort) > 1:
        arrayCenter = len(arrayToSort) // 2

        leftArray = arrayToSort[arrayCenter:]
        rightArray = arrayToSort[:arrayCenter]
        mergeSort(leftArray)
        mergeSort(rightArray)

        i = 0
        j = 0
        k = 0

        while i < len(leftArray) and j < len(rightArray):
            if leftArray[i] < rightArray[j]:
                arrayToSort[k] = leftArray[i]
                i += 1
            else:
                arrayToSort[k] = rightArray[j]
                j += 1
            k += 1

        while i < len(leftArray):
            arrayToSort[k] = leftArray[i]
            i += 1
            k += 1

        while j < len(rightArray):
            arrayToSort[k] = rightArray[j]
            j += 1
            k += 1


array = [38,27,43,3,9,82,10]
mergeSort(array)
print(array)