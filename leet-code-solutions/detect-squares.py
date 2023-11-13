class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        
    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1  

    def count(self, point: List[int]) -> int:
        square = 0
        x1, y1 = point

        for (x2, y2), n in self.points.items():
            x_dist, y_dist = abs(x1 - x2), abs(y1 - y2)

            if x_dist == y_dist and x_dist > 0:
                c1 = (x1, y2)
                c2 = (x2, y1)

                if c1 in self.points and c2 in self.points:
                    square += n * self.points[c1] * self.points[c2]

        return square
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)