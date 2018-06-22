x=y=GCD=0

def extendedEuclidean(a,b):
    global x,y
    if b==0:
        x=1
        y=0
        GCD = a
        return

    extendedEuclidean(b,a%b)

    cur_x = y
    cur_y = x - (a/b)*y

    x = cur_x
    y = cur_y
    

# 18x + 30y = 6
#find x and y
extendedEuclidean(18,30)
print("For the given eq, x = "+str(x)+" and y = "+str(y))
