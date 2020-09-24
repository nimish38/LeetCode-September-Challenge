class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        t = list(t)
        # remove each letter in s from t, remaining letter is answer
        for letter in s:
            t.remove(letter)
        return t[0]    
            