class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [amount+1]*(amount+1)
        dp[0] = 0
        for i in range(1,len(dp)):
            for j in coins:
                if i>=j:
                    dp[i] = min(dp[i], dp[i-j]+1)
        return dp[amount] if dp[amount]<=amount else -1