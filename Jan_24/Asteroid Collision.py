class Solution:
    def asteroidCollision(self, asteroids):
        stack, top = [], -1
        for ast in asteroids:
            if top is -1:
                stack.append(ast)
                top += 1
            else:
                if ast < 0:
                    if stack[top] < 0:
                        stack.append(ast)
                        top += 1
                    else:
                        while top >= 0 and stack[top] < abs(ast):
                            stack.pop()
                            top -= 1

                        if top is -1:
                            stack.append(ast)
                            top += 1
                        else:
                            if stack[top] == abs(ast):
                                stack.pop()
                                top -= 1
                else:
                    if stack[top] > 0:
                        stack.append(ast)
                        top += 1
                    else:
                        while top >= 0 and abs(stack[top]) < ast:
                            stack.pop()
                            top -= 1

                        if top is -1:
                            stack.append(ast)
                            top += 1
                        else:
                            if abs(stack[top]) == ast:
                                stack.pop()
                                top -= 1
        return stack

print(Solution().asteroidCollision([-2,-1,1,2]))