class Solution:
    def asteroidCollision(self, asteroids):
        stack, top = [asteroids[0]], 0
        for i in range(1, len(asteroids)):
            if asteroids[i] > 0:
                stack.append(asteroids[i])
                top += 1
            else:
                while top >= 0 and stack[top] < abs(asteroids[i]):
                    stack.pop()
                    top -= 1
                if stack[top] == abs(asteroids[i]):
                    stack.pop()
                    top -= 1
                    continue
                if top == -1:
                    stack.append(asteroids[i])
                    top+= 1
        return stack

print(Solution().asteroidCollision([10,2,-5]))