import sys
l=4
dp = [0]*(l+1)
len_wise_profit = {0:0,1:2,2:3,3:2,4:5}

def maxProfit(s,e,kitni_baar_kata):
    print(s,e,kitni_baar_kata)
    if kitni_baar_kata==l:
        return
    if dp[kitni_baar_kata]!=0:
        return dp[kitni_baar_kata]
    dp[kitni_baar_kata]=-sys.maxsize
    for k in range(s,e+1):
        dp[kitini_baar_kata]=max(dp[kitni_baar_kata],maxProfit(s,k,kitni_baar_kata+1)+maxProfit(k+1,e,kitni_baar_kata+1)+len_wise_profit[k-s]+len_wise_profit[e-(k+1)])
    return dp[s-1][e-1]

print(maxProfit(0,4,0))
