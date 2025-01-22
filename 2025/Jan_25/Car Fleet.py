class Solution:
    def carFleet(self, target: int, position, speed) -> int:
        combo, i = [], 0
        for i in range(len(speed)):
            combo.append((position[i], speed[i]))
        combo.sort(key=lambda x: x[0])

        st, i = [(target - combo[i][0]) / combo[i][1]], i - 1
        while i >= 0:
            time = (target - combo[i][0]) / combo[i][1]
            if time > st[-1]:
                st.append(time)

        return len(st)



