#1. Two Sum

# Brute Force Solution
def solution_BF(array , target):
    for i in range(len(array)):
        for j in range(i+1 , len(array)):
            sum = array[i] + array[j]
            if sum == target:
                return [i,j]



# Hash Map's Solution