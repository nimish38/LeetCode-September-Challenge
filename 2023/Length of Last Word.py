class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = []
        # add all words in a list
        for word in s.split(' '):
            if len(word) > 0:
                words.append(word)
        # if there's no word        
        if len(words) == 0:
            return 0
        # return last word length
        return len(words[len(words) -1])        