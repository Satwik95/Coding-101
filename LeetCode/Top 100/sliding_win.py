class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if nums==[]: return []
        d = collections.deque()
        res = []
        # set the window first
        for i in range(k):
            # remove the elements snaller than the cur candidate from the right
            while d and nums[i]>=nums[d[-1]]:
                d.pop()
            d.append(i)
            # for the remaining elements
        for i in range(k, len(nums)):
            # first element in the deque is the max
            res.append(nums[d[0]])
            # remove elements not in window from the left
            while d and d[0]<=i-k:
                d.popleft()
            # remove elements not a good candidate
            while d and nums[d[-1]]<=nums[i]:
                d.pop() 
            d.append(i)
        # append the last max element, since it didn't enter the loop
        res.append(nums[d[0]])
        return res
