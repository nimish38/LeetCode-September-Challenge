class Solution:
    def numTeams(self, rating) -> int:
        cnt, n = 0, len(rating)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                        cnt += 1
        return cnt



