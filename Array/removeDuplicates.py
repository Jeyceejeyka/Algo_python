# Problem: Remove all duplicates in-place but allow each element only twice

# Given a sorted array, modify it so each number appears at MOST twice, return the new length.

# def removeDuplicates(nums):
#     result = []
    
#     left = 0
#     # right = len(nums) - 1
    
    
#     while left <= len(nums) - 1:
#         if nums[left] not in result:
#             result.append(nums[left])
#             left += 1
#         else:
#             count = result.count(nums[left])
#             if count < 2:
#                 result.append(nums[left])
#             left += 1
#     for i in range(len(result)):
#         nums[i] = result[i] 
#     return len(result)

# But here is a REAL two pointer O(1) space
def removeDuplicates(nums):
    write = 0

    for n in nums:
        if write < 2 or n != nums[write-2]:
            nums[write] = n
            write += 1

    return write


print(removeDuplicates([1,1,1,2,2,3,3,3,3,4]))
print(removeDuplicates([0,0,1,1,1,1,2,2,3,3,4,4]))
    
    
# Example Input
# nums = [1,1,1,2,2,3,3,3,3,4]

# Expected array (in-place)
# [1,1,2,2,3,3,4]

# Expected return value
# 7