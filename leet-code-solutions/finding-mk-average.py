from sortedcontainers import SortedList

class MKAverage:

    def __init__(self, m: int, k: int):
        self.left = SortedList()
        self.mid = SortedList()
        self.right = SortedList()
        self.total = deque()
        self.m = m
        self.k = k
        self.sum = 0

    def addElement(self, num: int) -> None:
        self.total.append(num)
        k = self.k
        m = self.m

        self.left.add(num)
        if len(self.left) > k:
            el = self.left.pop()
            self.mid.add(el)
            self.sum += el
        if len(self.mid) > m - 2*k:
            el = self.mid.pop()
            self.right.add(el)
            self.sum -= el
        
        
        if len(self.total) > m:
            last = self.total.popleft()

            if self.left[-1] >= last:
                self.left.remove(last)
            elif self.mid[-1] >= last:
                self.mid.remove(last)
                self.sum -= last
            else:
                self.right.remove(last)
            

            if len(self.left) < k:
                self.sum -= self.mid[0]
                self.left.add(self.mid[0])
                self.mid.remove(self.mid[0])
            if len(self.mid) < m - 2*k:
                self.sum += self.right[0]
                self.mid.add(self.right[0])
                self.right.remove(self.right[0])
            
       
    def calculateMKAverage(self) -> int:
        if len(self.total) < self.m:
            return -1
        return self.sum // len(self.mid)


# Your MKAverage object will be instantiated and called as such:
# obj = MKAverage(m, k)
# obj.addElement(num)
# param_2 = obj.calculateMKAverage()