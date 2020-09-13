class Solution:
    def insert(self, intervals: List[List[int]], I: List[int]) -> List[List[int]]:
        res, i = [], -1
        for i, (x, y) in enumerate(intervals):
            # if new interval starts after end of cuurent, add current to result
            if y < I[0]:
                res.append([x, y])
            # if end of new interval ends before current interval starts,
            # add remainig current intervals as it is and break  
            elif I[1] < x:
                i -= 1
                break
            # set starts and end for current and new interval overlaappings    
            else:
                I[0] = min(I[0], x)
                I[1] = max(I[1], y)
                
        return(res + [I] + intervals[i+1:])