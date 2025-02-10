class Solution:
    def deleteAndEarn(self, nums) -> int:
        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 2

        def solve(cnt):
            if not cnt:
                return 0
            score, best = 0, -1
            for val in cnt:
                prev, pcnt, nex, ncnt, score = val - 1, 0, val + 1, 0, val
                cnt[val] -= 1
                if cnt[val] == 0:
                    del cnt[val]
                if prev in cnt:
                    pcnt = cnt[prev]
                    del cnt[prev]
                if nex in cnt:
                    ncnt = cnt[nex]
                    del cnt[nex]
                score += solve(cnt)
                if pcnt > 0:
                    cnt[prev] = pcnt
                if ncnt > 0:
                    cnt[nex] = ncnt
                if val not in cnt:
                    cnt[val] = 1
                else:
                    cnt[val] += 1
                best = max(best, score)
            return best

        return solve(nums)