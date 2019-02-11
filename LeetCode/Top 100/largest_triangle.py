class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        return max(0.5*abs(x[0]*y[1] + y[0]*z[1] + z[0]*x[1] \
                    -x[0]*z[1] - z[0]*y[1] - y[0]*x[1]) for x, y, z in itertools.combinations(points, 3))