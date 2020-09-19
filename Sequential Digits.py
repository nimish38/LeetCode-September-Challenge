class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def get_elements(size, l, h):
            res = []
            # until size is less than high
            while(size <= len(str(h))):
                i = 1
                # until the last digit is 9
                while(i+size <= 10):
                    j = i
                    num = ''
                    # generate sequences of size = size
                    for k in range(j, j+size):
                        num += str(k)  
                    # if sequence generated is between range, add to result    
                    if l <= int(num) <= h:
                        res.append(int(num))
                    i += 1
                size +=1    
            return res
                         
        # get num of digits in low    
        size = len(str(low))
        res = get_elements(size, low, high)
        return res