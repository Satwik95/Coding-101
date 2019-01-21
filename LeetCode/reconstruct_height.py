class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort()

        n = len(people)
        table = [i for i in range(n)]  # store the final positions
        res = [None] * n

        while people:
            top = people.pop(0)
            stack = [top]
            # find the same height
            while people and people[0][0] == stack[0][0]:
                stack.append(people.pop(0))

            # put them in the final position
            while stack:
                top = stack.pop()
                idx = top[1]
                print(stack, idx)
                res[table.pop(idx)] = top  # put in the final position

        return res

s = Solution()
print(s.reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]))

