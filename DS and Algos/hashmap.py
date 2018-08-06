class HashMap:
    def __init__(self,size):
        self.size = size
        self.map = [None]*self.size
        
    def my_hash(self,key):
        res = 0
        for i in range(len(key)):
            #in anagrams the hash val will always be same,
            #hence we are multiplying the weight factor i.e the position in this case
            res+=(ord(key[i])*i)
        return res%self.size
    
    def rehash(self,oldhash):
        return (oldhash+1)%self.size#linear probing
    
    def add(self,key,val):
        #I can also use prehash concept to make sure that all the key are non negative key=hash(key),
        #and then use my custom hash function
        key_hash = self.my_hash(key)
        #if key does not exist
        if self.map[key_hash]==None:
            self.map[key_hash] = [(key,val)]
        else:
            i=0
            for k,v in self.map[key_hash]:
                #if the key is same for the same hash, update the value
                if k==key:
                    self.map[key_hash][i] = (key,val)
                    return
                i+=1
            #diff key same hash
            #you can find nextslot by rehashing or do chaining
            self.map[key_hash].append((key,val))

    def get(self,key):
        key_hash = self.my_hash(key)
        if self.map[key_hash]==None:
            return False
        else:
            i=0
            for k,v in self.map[key_hash]:
                #if the key is same for the same hash, update the value
                if k==key:
                    return key,v
                i+=1
        
    def delete(self,key):
        key_hash = self.my_hash(key)
        #if key does not exist
        if self.map[key_hash]==None:
            return
        else:
            i=0
            for k,v in self.map[key_hash]:
                #if the key is same for the same hash, update the value
                if k==key:
                    del self.map[key_hash][i]
                    if not self.map[key_hash]:
                        self.map[key_hash] = None
                    return
                i+=1

if __name__=="__main__":
    h = HashMap(10)
    h.add("satwik",20)
    h.add("kiwtas",30)
    h.add("satwik",40)
    print(h.get("kiwtas"))
    h.delete("satwik")
