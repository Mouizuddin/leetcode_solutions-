# 704. Binary Search
'''
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
'''

def binary_search(array , key):
    array.sort()
    low = 0
    high = len(array)-1
    found = False
    while (low <= high) and not found:
        mid = (low + high) // 2

        if key == array[mid]:
            found = True
        elif key > array[mid]:
            low = mid + 1
        else:
            high = mid - 1
    if found == True:
        print(array.index(key))
    else:
        print(-1)
