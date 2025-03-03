from collections import defaultdict


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        curr, mol, num, st, i = defaultdict(int), '', '', [], 0
        while i < len(formula):
            c = formula[i]
            if c.isnumeric():
                num += c
            if c.isalpha():
                if mol and num:
                    curr[mol] += int(num)
                    mol, num = '', ''
                if c.isupper() and mol:
                    curr[mol] += 1
                    mol = ''
                mol += c
            if c == '(':
                if mol and num:
                    curr[mol] += int(num)
                elif mol:
                    curr[mol] += 1
                st.append(curr)
                curr, mol, num = defaultdict(int), '', ''
            if c == ')':
                if mol and num:
                    curr[mol] += int(num)
                elif mol:
                    curr[mol] += 1
                suffix, i = '', i + 1
                while i < len(formula) and formula[i].isnumeric():
                    suffix += formula[i]
                    i += 1
                if suffix:
                    for ele in curr:
                        curr[ele] *= int(suffix)
                prev = st.pop()
                for ele in curr:
                    prev[ele] += curr[ele]
                curr, mol, num = prev, '', ''
                i -= 1
            i += 1
        if num:
            curr[mol] += int(num)
        else:
            curr[mol] += 1

        res, keys = '', list(curr.keys())
        keys.sort()
        for val in keys:
            res += val
            if curr[val] > 1:
                res += str(curr[val])
        return res


print(Solution().countOfAtoms(formula = "Mg(H2O)N"))



