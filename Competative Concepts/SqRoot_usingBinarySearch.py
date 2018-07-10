def sqRt(val,p):
    start=0
    end=val
    ans = None
    #for int part
    while(start<=end):
        mid = int((start+end)/2)
        if mid*mid==val:
            return ans
        elif mid*mid>val:
            end=mid-1
        else:
            ans = mid
            start = mid+1
    #for fractional part
    inc = 0.1
    for i in range(0,p):
        while ans*ans<=val:
            ans+=inc
        ans-=inc
        inc/=10
    x = "%0."+str(p)+"f"
    return x%ans

if __name__ == "__main__":
    print(sqRt(3,6))
