class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id) -> int:
        hashmap, st, total = {}, [], 0
        for emp in employees:
            hashmap[emp.id] = [emp.importance, emp.subordinates]
        st.append(id)
        while st:
            node = st.pop()
            total += hashmap[node][0]
            st.extend(hashmap[node][1])
        return total


a, b, c = Employee(1,5,[2,3]), Employee(2,3,[]), Employee(3,3,[])
print(Solution().getImportance([a, b, c], 1))