import math


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}
        for num in nums:
            if num in h:
                h[num] += 1
            else:
                h[num] = 1

        YOLO = math.ceil(len(nums) / 2)

        for key in h:
            if h[key] > YOLO:
                return key


s = Solution()
print(s.majorityElement([3, 2, 3]))
