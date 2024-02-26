class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s_nums = []
        # convert int to string and sort is desc order
        for i in nums:
            s_nums.append(str(i))
        s_nums.sort(reverse = True) 
        
        # for case where '30' > '3', but 330 > 303 : check each pair and swap if a case found
        # continue until there's no change in s_nums for 2 consecuive runs
        change_flag = True
        while change_flag == True:
            change_flag = False
            for i in range(len(s_nums)-1):
                if int(s_nums[i+1]+ s_nums[i]) > int(s_nums[i]+ s_nums[i+1]):
                    s_nums[i], s_nums[i+1] = s_nums[i+1], s_nums[i]
                    change_flag = True
        
        return str(int(''.join(s_nums)))