class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pre = []
        suf = []
        for n in nums:
            if pre:
                pre.append(pre[-1]*n)
            else:
                pre.append(n)
        print(pre)
        for n in nums[::-1]:
            if suf:
                suf.append(suf[-1]*n)
            else:
                suf.append(n)
                
        suf = suf[::-1]
        print(suf)
        res = []
        for i in range(len(nums)):
            if i== 0:
                res.append(suf[i+1])
            if i == len(nums)-1:
                res.append(pre[i-1])
            else:
                res.append(pre[i-1]*suf[i+1])
        return res

print(Solution().productExceptSelf([1,2,3,4]))
