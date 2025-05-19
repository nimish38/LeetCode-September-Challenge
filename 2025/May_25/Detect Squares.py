from collections import defaultdict


class DetectSquares(object):

    def __init__(self):
        self.cord = defaultdict(int)
        self.pts = []

    def add(self, point):
        a, b = point
        self.cord[(a, b)] += 1
        self.pts.append(point)

    def count(self, point):
        cnt = 0
        a, b = point
        for x, y in self.pts:
            if abs(a - x) != abs(b - y) or x== a or y == b:
                continue
            cnt += self.cord[(x, b)] * self.cord[(a, y)]
        return cnt