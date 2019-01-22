class Solution(object):
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        from collections import Counter
        occ = dict(Counter(str(N)))
        sudo = 0
        exp = 0
        while sudo<=10**9:
            sudo = 2**exp
            exp += 1
            if occ == dict(Counter(str(sudo))):
                return True
        return False