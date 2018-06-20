""" Solve in logN time"""

def power(a,b):

    if b==0:
        return 1

    res = power(a,b/2)
    res*=res

    if b%2!=0:
        res*=a

    return res


