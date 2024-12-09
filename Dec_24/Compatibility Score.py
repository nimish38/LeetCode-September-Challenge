class Solution:
    def maxCompatibilitySum(self, students, mentors) -> int:
        maxsum, seen, n = 0, set(), len(students)
        for i in range(n):
            curr, ind = 0, -1
            for j in range(n):
                if j in seen:
                    continue
                compat = compatibility(students[i], mentors[j])
                if compat > curr:
                    curr, ind = compat, j
            maxsum += curr
            seen.add(ind)

        return maxsum