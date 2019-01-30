class Solution(object):
    
    def __init__(self):
        self.res = []
    
    def dfs(self, nums, path):
        if nums == []:
            #print(path)
            self.res.append(path)
        for i in range(len(nums)):
            #print(path)
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]])
            
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.dfs(nums, [])
        return self.res

print(Solution().permute([1,2,3]))
