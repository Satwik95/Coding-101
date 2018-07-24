def f():
    for i in range(5):
        for j in range(5):
            print(i,j)
            if i==3:
                return

f()
