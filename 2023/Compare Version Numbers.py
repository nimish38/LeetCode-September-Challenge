class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # get integer representation for each version
        v1 = list(map(int,version1.split('.')))
        v2 = list(map(int,version2.split('.')))
        
        # if version lengths are unequal, append trailing zeroes
        if len(v1) > len(v2):
            for i in range(len(v1)-len(v2)):
                v2.append(0)      
        elif len(v2) > len(v1):
            for i in range(len(v2)-len(v1)):
                v1.append(0)        
        
        # compare respective numbers and return bigger number
        for i in range(len(v1)):
            if v1[i] > v2[i]:
                return 1
            elif v1[i] < v2[i]:
                return -1
        return 0    
                
        