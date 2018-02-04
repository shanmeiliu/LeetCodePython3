class Solution:
    def twoSum(self, nums, target):
        """
        Approach #2 (Two-pass Hash Table)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for i, num in enumerate(nums):
            #print(i,num)
            #print(lookup)
            lookup[num] = i
        for i, num in enumerate(nums):
            if target-num in lookup and lookup[target-num]!=i:
                #return [lookup[target - num], i] also works
                return (lookup[target - num], i)
            
