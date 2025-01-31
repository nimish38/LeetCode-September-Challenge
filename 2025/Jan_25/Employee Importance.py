from collections import defaultdict

class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id) -> int:
        hashmap, st, total = defaultdict(list), [], 0
        for emp in employees:
            hashmap[emp.id].append(emp.importance, emp.subordinates)
        st.append(id)
        while st:
            node = st.pop()
            total += hashmap[node][0]
            st.extend(hashmap[node][1])
        return total
