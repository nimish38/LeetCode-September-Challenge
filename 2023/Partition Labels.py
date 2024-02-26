class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        # finding last occurences of each char in the string
        last = {}
        for i in range(len(S)):
            last[S[i]] = i
        ans = []
        partition = 0

        for i in range(len(S)):

            # find last position of a letter
            curr = S[i]
            curr_last = last[curr]
            if curr_last > partition:
                partition = curr_last

            # if position is last position of group, create partition    
            if i == partition:
                ans.append(i+1)
           # print(i,curr,curr_last,partition)    
        
        sum = 0
        final = []
        # remove extra index numbers added
        for part in ans:
            final.append(part - sum)
            sum = part
        return(final)    
            
        