class Solution:
    def maxCompatibilitySum(self, students, mentors) -> int:
        maxsum, seen, n = 0, set(), len(students)

        def compatibility(a, b):
            val = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    val += 1
            return val

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