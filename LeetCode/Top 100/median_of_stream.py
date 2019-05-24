from heapq import *

class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.heap = [], []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        small, large = self.heap
        heappush(small, -heappushpop(large, num))
        if len(large)<len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        """
        :rtype: float
        """
        small, large = self.heap
        if len(large)>len(small):
            return large[0]
        else:
            return float((large[0]-small[0])/2.0)


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()