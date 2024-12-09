class Solution:
    def maxCompatibilitySum(self, students, mentors) -> int:
        self.maxsum, n = 0, len(students)
        
        def compatibility(a, b):
            val = 0
            for i in range(len(a)):
                if a[i] == b[i]:
                    val += 1
            return val

        def solve(ind, score, seen):
            if ind >= n:
                self.maxsum = max(self.maxsum, score)
            else:
                for i in range(n):
                    if i in seen:
                        continue
                    else:
                        seen.add(i)
                        score += compatibility(students[ind], mentors[i])
                        solve(ind + 1, score, seen)
                        seen.remove(i)

        solve(0, 0, set())
        return self.maxsum

print(Solution().maxCompatibilitySum(students = [[1,1,0],[1,0,1],[0,0,1]], mentors = [[1,0,0],[0,0,1],[1,1,0]]))