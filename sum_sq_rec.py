def sum_sq(n):
    if n==1:
        return 1
    return n*n + sum_sq(n-1)

print(sum_sq(10))

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    
    h = {}
    for key in nums:
        h[key] = 0

    #print(len(h))
    for i in range(len(nums)):
        if target-nums[i] in h:
            if h[(target-nums[i])] == 1:
                return [nums.index(target-nums[i]), i]
            else:
                h[nums[i]] = 1
            
    return x

print(twoSum([7, 12, 11, 1], 13))
