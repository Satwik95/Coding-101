class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<4:
            return n
        sqs = []
        for i in range(1,n):
            temp = i*i
            if temp>n:
                break
            sqs.append(temp)
        dp = [i for i in range(n+1)]
        for i in range(4,n+1):
            for j in sqs:
                dp[i] = min(dp[i], dp[i-j]+1)
        return dp[-1]