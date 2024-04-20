import bisect
class Solution:
    def suggestedProducts(self, products, searchWord: str):
        products.sort()
        res = []
        prefix = ""
        for c in searchWord:
            prefix += c
            index = bisect.bisect_left(products, prefix)
            res.append([w for w in products[index: index + 3] if w.startswith(prefix)])
        return res


print(Solution().suggestedProducts(products = ["havana"], searchWord = "havana"))