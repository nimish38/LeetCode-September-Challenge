class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        # remove each letter in s from t, remaining letter is answer
        for letter in s:
            t.remove(letter)
        return t[0]    
        
        #optimised approach
        s_asci, t_asci = 0, 0
        for i in s:
            s_asci += ord(i)
        for i in t:
            t_asci += ord(i)
            
        return chr(t_asci - s_asci)    
            