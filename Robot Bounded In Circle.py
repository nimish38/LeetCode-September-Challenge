class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # x,y are robot cordinates
        # dx, dy are delta or changes after instruction
        dx, dy, x, y = 0, 1, 0, 0
        for l in 4*instructions:
            # increase dy since robot's moving ahead
            if l == "G": 
                x, y = x+dx, y+dy
            # change direction     
            elif l == "L":
                dx, dy = -dy, dx
            else:
                dx, dy = dy, -dx
        # if robot returns at origin after 4 loops max,true else false        
        return (x,y) == (0,0)