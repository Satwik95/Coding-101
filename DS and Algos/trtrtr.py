import turtle

def tree(x,d):
    if d==0:
        t.circle(10)
        return
    else:
        t.fd(x)
        t.left(30)
        tree(x/2,d-1)
        t.right(60)
        tree(x/2,d-1)
        t.left(30)
        t.bk(x)

def f(x,d):
    if d==0:
        for i in range(3):
            t.fd(x)
            t.left(120)
        return
    else:
        f(x/2,d-1)
        t.fd(x/2)
        f(x/2,d-1)
        t.bk(x/2)
        t.left(60)
        t.fd(x/2)
        t.right(60)
        f(x/2,d-1)
        t.left(60)
        t.bk(x/2)
        t.right(60)


t = turtle.Turtle()
f(100,2)
        
