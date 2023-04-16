class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        freq = Counter(deck)

        arr = []
        for value in freq.values():
            arr.append(value)
        
        a = min(arr)
        if a < 2:
            return False
        for i in range(2, a + 1):
            if all(val % i == 0 for val in arr):
                return True

        return False