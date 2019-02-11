class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []
        res = set()
        nums.sort()
        for i in range(len(nums)-2):
            if i==0 or nums[i]>nums[i-1]:
                s, e = i+1, len(nums)-1
                while s<e:
                    if nums[s] + nums[e] + nums[i] == 0:
                        res.append([nums[i], nums[s], nums[e]])
                        s += 1
                        e -= 1
                    elif nums[s] + nums[e] + nums[i] < 0:
                        temp = s
                        while nums[s] == nums[temp] and s<e:
                            s += 1
                    else:
                        temp = e
                        while nums[e] == nums[temp] and s<e:
                            e -= 1
        return res