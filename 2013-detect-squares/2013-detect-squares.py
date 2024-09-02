class DetectSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []
        

    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)
        

    def count(self, point: List[int]) -> int:
        result = 0
        px, py = point
        for x, y in self.pts:
            if ((abs(px-x) != abs(py-y)) or x == px or y == py):
                continue
            result += self.ptsCount[(x,py)] * self.ptsCount[(px,y)]
        return result
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)