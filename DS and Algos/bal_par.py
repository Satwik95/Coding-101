def isPair(op,cl):
    if op=="(" and cl==")":
        return True
    if op=="[" and cl=="]":
        return True
    if op=="{" and cl=="}":
        return True
    return False

def isBalanced(s):
    stack = []
    for i in range(len(s)):
        if s[i]=="{" or s[i]=="[" or s[i]=="(":
            stack.append(s[i])
        elif s[i]=="}" or s[i]=="]" or s[i]==")":
            if not stack or isPair(stack[-1],s[i])==False:
                return False
            else:
                stack.pop()
    return True if not stack else False


print(isBalanced("{{[[(())]]}}"))
