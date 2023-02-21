#1. Two Sum
'''
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
'''
# Brute Force Solution
def solution_BF(array , target):
    for i in range(len(array)):
        for j in range(i+1 , len(array)):
            sum = array[i] + array[j]
            if sum == target:
                return [i,j]



# Hash Map's Solution

