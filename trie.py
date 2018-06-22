class node:
    def __init__(self,data):
        self.isTerminal = False
        self.data = data
        self.h = {}

class Trie:
    
    def __init__(self):
        self.root = node(None)
    
    def addWord(self,word):
        temp = self.root
        print(temp)
        for i in range(0,len(word)):
            ch = word[i]
            if ch not in temp.h:
                child = node(ch)
                temp.h[ch] = child
                temp = child
            else:
                temp = temp.h[ch]

        temp.isTerminal = True

    def search(self,word):
        temp = self.root
        for i in range(0,len(word)):
            ch = word[i]
            if ch not in temp.h:
                return False
            else:
                temp = temp.h[ch]
                
        return temp.isTerminal
                        
words = ["apple","ape","coder","satwik"]
global root
t = Trie()

for x in words:
    t.addWord(x)

