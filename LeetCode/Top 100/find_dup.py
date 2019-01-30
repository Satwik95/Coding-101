class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def check_xor(nums):
            
            if nums == []:
                return
            #print(nums)
            res = nums[0]
            for x in nums[1:]:
                res ^= x
            print(nums, res)
            return res
        
        init_xor = check_xor(nums)
        temp = list(set(nums))
        print(temp, init_xor)
        for i in range(len(temp)):
            val = check_xor(temp[:i]+temp[i+1:])
            if val == init_xor:
                return temp[i]

print(Solution().findDuplicate([[1,4,4,2,4]]))
