class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        l = A
        n = len(l)
        result = []
        c = n * [0]

        result.append(list(l))

        # calculate all possible 24 combinations
        i = 0;
        while i < n:
            if c[i] < i:
                if i % 2 == 0:
                    tmp = l[0]
                    l[0] = l[i]
                    l[i] = tmp

                else:

                    tmp = l[c[i]]
                    l[c[i]] = l[i]
                    l[i] = tmp
                # store all permutations in result    
                result.append(list(l))
                c[i] += 1
                i = 0
            else:
                c[i] = 0
                i += 1


        mx = -1
        ind =-1
        # calculating if solution has valid time
        for i in range(len(result)):
            soln = result[i]
            hrs = soln[0]*10 + soln[1]
            mins = soln[2]*10 + soln[3]
            if(hrs < 24 and mins <60):
                # calculating max time solution
                val = hrs*60 + mins 
                #print(soln, val)
                if val > mx:
                    mx = val
                    ind = i
        if ind == -1:
            return ""
        else:
            return str(result[ind][0])+str(result[ind][1])+":"+str(result[ind][2])+str(result[ind][3])