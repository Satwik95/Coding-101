t = int(input())

for j in range(t):
    ans=0
    n = int(input())
    for i in range(1,n+1):
        ans += n/(i*1.0)
    print("%.2f" % ans)
