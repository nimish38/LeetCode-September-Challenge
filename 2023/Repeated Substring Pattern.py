class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        b = set(list(s))
        
        # single element cant have a subset
        if n==1:
            return False
        # if there is a single letter, repeated pattern is always possible
        if len(b)==1:
            return True
        
        else:
            #check for pattern till half length
            for i in range(2,(n//2)+1):
                x = s[:i]
                cnt = n//i
                #print(x,cnt,x*cnt)
                if x*cnt == s:
                    return True
            return False
                