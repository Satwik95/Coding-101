import sys
class ConvexHull:
    def checkOrientation(self,p,q,r):
        slope_diff = int(((q[1]-p[1])*(r[0]-q[0]))-((q[0]-p[0])*(r[1]-q[1])))
        if slope_diff==0: return 0
        return 2 if slope_diff>0 else 1
        
    def jarvis(self,num):
        n=len(num)
        if n<3:
            return
        #find the left most point
        l= (sys.maxsize,0)
        next_q = 0
        for i in range(0,n):
            if num[i][0]<l[0]:
                l= num[i]
                next_q = i
        #select p,q,r and find the orientation
        #if the orientation from pq->qr is towards right then make r as q
        #iterate for all the points
        p=l#left most coord
        conv_hull = []
        while True:
            conv_hull.append(p)
            q = num[(next_q+1)%n]
            for i in range(0,n):
                if self.checkOrientation(p,q,num[i])==2:
                    q = num[i] #if moving towards the right
            p=q
            if p==l:
                break
        print("Boundary points:",conv_hull)

if __name__ == "__main__":
    j = ConvexHull()
    points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
    j.jarvis(points)
