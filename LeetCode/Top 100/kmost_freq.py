class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = {}
        for num in nums:
            d[num] = 0

        for num in nums:
            d[num] += 1

        l = sorted(d.items(), key= lambda x: x[1], reverse = True)

        #return [x[0] for x in l[:k]]
        import collections
        count = collections.Counter(nums)
        print(list(count.get))
        #return heapq.nlargest(k, count.keys(), key = count.get)

nums = [1,1,1,1,2,2,2,3]
print(Solution().topKFrequent(nums, 2))