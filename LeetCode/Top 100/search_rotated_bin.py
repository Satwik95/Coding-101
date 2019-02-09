class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start = 0
        end = len(nums)-1
        
        while start<=end:
            mid = int((start+end)/2)
            if nums[mid] == target:
                return mid
            # if mid is in the left seid
            if nums[start]<=nums[mid]:
                if nums[start]<= target <= nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            
            #if mid on the right side
            else:
                if nums[mid]<= target <= nums[end]:
                    start = mid+1
                else:
                    end = mid - 1
        return -1