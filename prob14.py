from random import uniform
from math import pow
import threading

def gen():
    return (uniform(-1,1),uniform(-1,1))

def ifInCircle(coord):
    x, y = coord[0], coord[1]
    # assuming unit circle
    return x*x + y*y < 1

def aprox(n):
    in_circle = 0
    in_sq = 0
    for _ in range(n):
        if ifInCircle(gen()):
            in_circle+=1
    return 4*(in_circle/n)


print("Enter no of iterations")
n = int(input())
"""
threads = [None]*1000
           
for i in range(len(threads)):
        threads[i] = threading.Thread(target=aprox, args = n)
        threads[i].start()

for i in range(len(threads)):
    threads[i].join()
"""
