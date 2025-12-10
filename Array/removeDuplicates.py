# Problem: Remove all duplicates in-place but allow each element only twice

# Given a sorted array, modify it so each number appears at MOST twice, return the new length.

def removeDuplicates(nums):
    result = []
    
    left = 0
    # right = len(nums) - 1
    
    
    while left <= len(nums) - 1:
        if nums[left] not in result:
            result.append(nums[left])
            left += 1
        else:
            count = result.count(nums[left])
            if count < 2:
                result.append(nums[left])
            left += 1
    for i in range(len(result)):
        nums[i] = result[i] 
    return len(result)

print(removeDuplicates([1,1,1,2,2,3,3,3,3,4]))
print(removeDuplicates([0,0,1,1,1,1,2,2,3,3,4,4]))
    
    
# Example Input
# nums = [1,1,1,2,2,3,3,3,3,4]

# Expected array (in-place)
# [1,1,2,2,3,3,4]

# Expected return value
# 7