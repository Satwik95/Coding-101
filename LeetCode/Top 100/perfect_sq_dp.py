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
        """dp = [i for i in range(n+1)]
        for i in range(4,n+1):
            for j in sqs:
                dp[i] = min(dp[i], dp[i-j]+1)
        return dp[-1]"""
        # using bfs
        count = 0
        frontier = [n]
        while frontier:
            count += 1 # for each level we are going down increment count
            temp = set()
            for u in frontier:
                for v in sqs:
                    if u==v:
                        return count
                    if u<v:
                        break
                    temp.add(u-v)
            frontier = temp    
        return count