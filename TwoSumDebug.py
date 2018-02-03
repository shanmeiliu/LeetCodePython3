print("Hello World!")

def twoSum( nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        print(i,num)
        print(lookup)
#key in d
#Return True if d has a key key, else False.
        if target - num in lookup:
            print(lookup)
            return [lookup[target - num], i]
        lookup[num] =i
print(twoSum([3,6,4,2],6))
"""
output
Hello World!
0 3
{}
1 6
{3: 0}
2 4
{3: 0, 6: 1}
3 2
{3: 0, 4: 2, 6: 1}
{3: 0, 4: 2, 6: 1}
[2, 3]

"""
