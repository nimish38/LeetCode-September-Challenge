class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pat = list(pattern)
        st = list(str.split())
        
        # if length of both are unequal or have unequal unique element count
        if((len(set(pat)) != len(set(st))) or (len(pat) != len(st))):
            return False        
        else:
            
            # get all indexes of each element
            pos = {k: [] for k in (set(pat))}
            for i in range(len(pat)):
                pos[pat[i]].append(i)
                
            # checking all indexes have matching values
            for pappu in pos.values():
                a = st[pappu[0]]
                for i in range(1,len(pappu)):
                    if st[pappu[i]] != a:
                        #print(a, st[pappu[i]])
                        return False
            return True        