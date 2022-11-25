def bubbleSortRecursive(arr: []):
    if len(arr) == 1:
        return arr

    for i in range(len(arr) - 1):
        if arr[i] <= arr[i + 1]:
            continue
        else:
            temp = arr[i]
            arr[i] = arr[i + 1]
            arr[i + 1] = temp

    a = arr[:-1]
    b = arr[-1]

    return bubbleSortRecursive(a) + [b]


def bubbleSortIterative(arr: []):
    length = len(arr) - 1
    for i in range(length):
        for j in range(length):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr


print(bubbleSortRecursive([2, 1, 5, 0, 24, 55, 2, 15, 6, 3, 11, 4, 9, 8, 2, 4, 10]))


# print(bubbleSortIterative([2, 1, 5, 0, 24, 55, 2, 15, 6, 3, 11, 4, 9, 8, 2, 4, 10]))

def selectionSort(arr: []):
    for i in range(len(arr)):
        min_value = arr[i]
        index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < min_value:
                min_value = arr[j]
                index = j
        temp = arr[i]
        arr[i] = min_value
        arr[index] = temp
    return arr


print(selectionSort([2, 1, 5, 0, 24, 55, 2, 15, 6, 3, 11, 4, 9, 8, 2, 4, 10]))


def insertionSort(arr: []):
    for i in range(1, len(arr)):
        temp = arr[i]
        temp_arr = arr[:i]
        if temp < arr[i - 1]:
            for j in range(len(temp_arr)):
                if temp_arr[j] > temp:
                    arr.pop(i)
                    arr.insert(j, temp)
                    break
    return arr


print(insertionSort([2, 1, 5, 0, 24, 55, 2, 15, 6, 3, 11, 4, 9, 8, 2, 4, 10]))


def mergeSort(arr: []):
    if len(arr) == 1:
        return arr

    # separate to left and right
    half = len(arr) // 2
    left_arr = arr[:half]
    right_arr = arr[half:]
    return merge(mergeSort(left_arr), mergeSort(right_arr))


def merge(left: [], right: []):
    arr = []

    while len(left) != 0 or len(right) != 0:
        if not left:
            arr.append(right[0])
            right.pop(0)
        elif not right:
            arr.append(left[0])
            left.pop(0)
        else:
            if left[0] < right[0]:
                arr.append(left[0])
                left.pop(0)
            else:
                arr.append(right[0])
                right.pop(0)
    return arr


"""
[2, 1, 5, 0, 24, 55, 2, 15] [6, 3, 11, 4, 9, 8, 2, 4, 10]
[2, 1, 5, 0] [24, 55, 2, 15]
[2, 1] [5, 0]
[2] [1]
[5] [0]
[24, 55] [2, 15]
[24] [55]
[2] [15]
[6, 3, 11, 4] [9, 8, 2, 4, 10]
[6, 3] [11, 4]
[6] [3]
[11] [4]
[9, 8] [2, 4, 10]
[9] [8]
[2] [4, 10]
[4] [10]
"""

print(mergeSort([2, 1, 5, 0, 24, 55, 2, 15, 6, 3, 11, 4, 9, 8, 2, 4, 10]))


def quickSort(arr: []):
    if len(arr) <= 1:
        return arr

    index = len(arr) - 1
    done = False

    while done is False:
        if index == 0:
            break
        for i in range(0, index):
            if i > index:
                done = True
            if arr[i] > arr[index]:
                temp = arr[i]
                arr.pop(i)
                arr.insert(index, temp)
                index -= 1
                if index > 1:
                    temp = arr[index - 1]
                    arr.pop(index - 1)
                    arr.insert(0, temp)
                break
            if i >= index - 1:
                done = True

    if len(arr) <= 3:
        return arr

    left = arr[:index]
    right = arr[index + 1:]

    return quickSort(left) + [arr[index]] + quickSort(right)


print(quickSort([2, 1, 5, 0, 24, 55, 2, 15, 6, 3, 11, 4, 9, 8, 2, 4, 10]))
# print(quickSort([4, 3]))

"""
#1 - Sort 10 schools around your house by distance:
insertion sort

#2 - eBay sorts listings by the current Bid amount:
radix or counting sort

#3 - Sort scores on ESPN
Quick sort

#4 - Massive database (can't fit all into memory) needs to sort through past year's user data
Merge Sort

#5 - Almost sorted Udemy review data needs to update and add 2 new reviews
Insertion Sort

#6 - Temperature Records for the past 50 years in Canada
radix or counting Sort
Quick sort if decimal places

#7 - Large user name database needs to be sorted. Data is very random.
Quick sort

#8 - You want to teach sorting
Bubble sort
"""