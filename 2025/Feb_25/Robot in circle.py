class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        face, pos, vals = 'N', [0, 0], {'00N': 1}
        moves = {
                    'N': {'G': [0, 1, 'N'], 'L': [0, 0, 'W'], 'R': [0, 0, 'E']},
                    'E': {'G': [1, 0, 'E'], 'L': [0, 0, 'N'], 'R': [0, 0, 'S']},
                    'S': {'G': [0, -1, 'S'], 'L': [0, 0, 'E'], 'R': [0, 0, 'W']},
                    'W': {'G': [-1, 0, 'W'], 'L': [0, 0, 'S'], 'R': [0, 0, 'N']}
                 }

        for _ in range(4):
            for c in instructions:
                change = moves[face][c]
                x, y, face = change[0], change[1], change[2]
                pos[0], pos[1] = pos[0] + x, pos[1] + y
                new_pos = str(pos[0]) + str(pos[1]) + face
            if new_pos in vals:
                return True
            vals[new_pos] = 1
        return False


print(Solution().isRobotBounded(instructions = "GG"))