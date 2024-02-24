class Solution:
    def asteroidCollision(self, asteroids):
        stack, i, top = [], 0, -1

        while i < len(asteroids) and asteroids[i] < 0:
            stack.append(asteroids[i])
            i += 1
        top = len(stack) - 1

        while i < len(asteroids):
            ast = asteroids[i]
            if ast > 0 or top is -1:
                stack.append(ast)
                top += 1
            else:
                if stack[top] < 0:
                    stack.append(ast)
                    top += 1
                else:
                    while top >= 0 and 0 < stack[top] < abs(ast):
                        stack.pop()
                        top -= 1
                    if top is -1 or stack[top] < 0:
                        stack.append(ast)
                        top += 1
                    else:
                        if stack[top] == abs(ast):
                            stack.pop()
                            top -= 1
            i += 1
        return stack

print(Solution().asteroidCollision([-2,-1,1,2,-3]))