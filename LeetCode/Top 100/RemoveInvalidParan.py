class Solution:
    
    def isPair(self,op,cl):
        return op=="(" and cl==")"

    def isBalanced(self,s):
        stack = []
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(s[i])
            elif s[i]==")":
                if stack==[] or self.isPair(stack[-1],s[i])==False:
                    return False
                else:
                    stack.pop()
        return stack==[]

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        
        parent = {s:None}
        level = {s:0}
        frontier = [s]
        j=1
        res = []
        while frontier:
            next = []
            for u in frontier:
                if(self.isBalanced(u)):
                    #print(u, level[u])
                    if res and level[u]>level[res[-1]]:
                        return res
                    res.append(u)
                    continue
                for i,ch in enumerate(u):
                    if ch==")" or ch=="(":
                        v = u[:i]+u[i+1:]
                        if v not in level:
                            level[v]=j
                            parent[v]=u
                            #print(v,level[v])
                            next.append(v)
            frontier = next
            j+=1
        return res
                    
                    
                    
