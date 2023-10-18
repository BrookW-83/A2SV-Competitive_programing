class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minVal = min(nums)
        maxVal = max(nums)

        maxVal -= k
        minVal += k

        return max(0, maxVal - minVal)
