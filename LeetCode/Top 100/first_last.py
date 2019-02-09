class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if nums == []:
            return [-1, -1]
        
        if len(nums)==1 and nums[0]==target:
            return [0, 0]
        
        def bin_search(rt=False):
            start = 0
            end = len(nums)-1
            while start<=end:
                mid = int((start+end)/2)
                if nums[mid] == target:
                    if rt:
                        if len(nums)>mid+1 and nums[mid+1]==target:
                            start = mid+1
                        else:
                            return mid
                    else:
                        if mid-1>=0 and nums[mid-1]==target:
                            end = mid-1
                        else:
                            return mid
                elif nums[mid]>target:
                    end  = mid -1
                else:
                    start = mid +1
            return -1
        
        first = bin_search()
        if first==-1:
            return [-1, -1]
        last = bin_search(True)
        return [first, last]

print(Solution().searchRange([2,2], 2))