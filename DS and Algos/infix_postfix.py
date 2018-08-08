def infix_postfix(infix):
    s = []
    postfix = ""
    operator = ["+","-","*","/"]
    prec = {"+":3,
            "-":2,
            "*":4,
            "/":5}
    for i in range(0,len(infix)):
        if infix[i] in operator:
            if s==[] or prec[infix[i]]>prec[s[-1]]:
                s.append(infix[i])
            else:
                while s!=[] and prec[infix[i]]<prec[s[-1]]:
                    postfix+=str(s[-1])
                    s.pop()
                s.append(infix[i])
        else:
            postfix+=str(infix[i])

    while s!=[]:
        postfix+=str(s.pop())
    return postfix


if __name__=="__main__":
    infix = input()
    print(infix_postfix(infix))
    # to convert infix to prefix:
    # reverse the infix->convert this to postfix->reverse this postfix
    #you will get your prefix
    
