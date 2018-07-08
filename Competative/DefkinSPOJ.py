""" delta x = |x_i - x_(i_1)| - 1 similarly for delta y
res = max del x * max del y
"""
def maxRect(X,Y,h,w):
    deltaX = []
    deltaY = []
    deltaX[0] = X[0]-0
    deltaX[len(X)]=abs(w-X[len(X)-1])
    deltaY[0] = Y[0]-0
    deltaY[len(Y)+1]=abs(h-Y[len(Y)-1])
    for i in range(0,len(X)):
        deltaX[i+1] = X[i]-x[i+1]

if name == "__main__":
    t = int(input())
    while t:
        w,h,n = input().split(" ")
        w = int(w)
        h = int(h)
        n = int(n)
        X = []
        Y = []
        for i in range(0,n):
            x,y = input().split(" ")
            x = int(x)
            y = int(y)
            X.append(x)
            Y.append(y)
        print(maxRect(X,Y,h,w))
        t-=1
