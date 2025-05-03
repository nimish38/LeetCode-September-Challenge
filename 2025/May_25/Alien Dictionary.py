from collections import defaultdict, deque


class Solution:
    def foreignDictionary(self, words) -> str:
        if len(words) == 1:
            return words[0]
        adj, indg = defaultdict(list), defaultdict(int)
        for i in range(len(words) - 1):
            first, second, flag = words[i], words[i + 1], False
            for j in range(min(len(first), len(second))):
                if first[j] not in adj:
                    adj[first[j]] = []
                if second[j] not in adj:
                    adj[second[j]] = []
                if first[j] != second[j]:
                    adj[first[j]].append(second[j])
                    indg[second[j]] += 1
                    flag = True
                    break
            if not flag and len(second) < len(first):
                return  ''
            k = j
            while k < len(first):
                if first[k] not in adj:
                    adj[first[k]] = []
                k += 1
            k = j
            while k < len(second):
                if second[k] not in adj:
                    adj[second[k]] = []
                k += 1

        que, res = deque(), ''
        for val in adj:
            if val not in indg:
                que.append(val)
                res += val

        while que:
            node = que.popleft()
            for nei in adj[node]:
                indg[nei] -= 1
                if indg[nei] == 0:
                    que.append(nei)
                    res += nei
                    del indg[nei]

        if len(indg) == 0:
            return res
        return ''

print(Solution().foreignDictionary(words=["abc","bcd","cde"]))