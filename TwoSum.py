class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            print(i,num)
            print(lookup)
            if target - num in lookup:
                print(lookup)
                return [lookup[target - num], i]
            lookup[num] = i
        
"""
Run Code Result:

Your input

[3,2,4]
6
Your stdout

0 3
{}
1 2
{3: 0}
2 4
{2: 1, 3: 0}
{2: 1, 3: 0}
Your answer

[1,2]
Expected answer

[1,2]
"""
