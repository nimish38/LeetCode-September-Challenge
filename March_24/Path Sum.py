class Solution:
    def pathSum(self, root, targetSum):
        stack, cnt = [(root, [])], 0
        while stack:
            item = stack.pop()
            if item[0].val == targetSum:
                cnt += 1
            for i in range(len(item[1])):
                if item[0].val + sum(item[1][:i + 1]) == targetSum:
                    cnt += 1

            lineage = item[1].insert(0, item[0].val)
            if item[0].right:
                stack.append((item[0].right, lineage))
            if item[0].left:
                stack.append((item[0].left, lineage))
        return cnt