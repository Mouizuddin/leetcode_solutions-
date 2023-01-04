# 13. Roman to Integer
'''
Input: s = "III"
Output: 3
Explanation: III = 3.
'''
def solution(string):
    roman = {
        "I": 1,
        "V": 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res= 0
    for i in range(len(string)):
        if i+1 < len(string) and roman[string[i]] < roman[string[i+1]]:
            res -= roman[string[i]]
        else:
            res += roman[string[i]]
    return res

print(solution('III'))