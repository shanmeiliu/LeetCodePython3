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
        
