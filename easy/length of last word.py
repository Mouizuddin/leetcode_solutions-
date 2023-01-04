# 58. Length of Last Word
'''
Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
'''

def solution(string):
    return len(string.strip().split()[-1])
