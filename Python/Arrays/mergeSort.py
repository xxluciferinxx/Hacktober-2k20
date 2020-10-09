# MERGE SORT (without in-place)
# Solution 1
# O(N(log(N)) time & space
def mergeSort(array):
    if len(array) == 1:
        return array
    middleIdx = len(array)//2
    leftHalf = array[:middleIdx]
    rightHalf = array[middleIdx:]
    return mergeSortedArray(mergeSort(leftHalf), mergeSort(rightHalf))

def mergeSortedArray(leftHalf, rightHalf):
    sortedArray = [None] * (len(leftHalf) + len(rightHalf))
    i = j = k = 0   # i, j, k pointers for left, right, and sortedArray[position] respectively
    while i < len(leftHalf) and j < len(rightHalf): # one of the left or right sub-array will be eliminated in end
        if leftHalf[i] <= rightHalf[j]:
            sortedArray[k] = leftHalf[i]
            i += 1
        else:
            sortedArray[k] = rightHalf[j]
            j += 1

        k += 1

    while i < len(leftHalf): # if left sub-array still have elements left fill them in final array
        sortedArray[k] = leftHalf[i]
        i += 1
        k += 1
    while j < len(rightHalf): # if right sub-array still have elements left in it, fill them in final array
        sortedArray[k] = rightHalf[j]
        j += 1
        k += 1

    return sortedArray

print(mergeSort([5,34,25,36,32,3,5,34,324,234,235,24543]))
print(mergeSort([5,1,4,5,4,234,25,345,343]))
