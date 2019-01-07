""" Solve in logN time"""
def power(a,b):
    print(a,b)
    if b==0:
        return 1

    res = power(a,int(b/2))
    res*=res
    print(res)
    if b%2!=0:
        res*=a

    return res

a = int(input())
b = int(input())
print(power(a,b))
