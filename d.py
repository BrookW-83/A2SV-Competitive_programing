class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num1 = 0
        num2 = 0

        for i in nums:
            num1 = (num1 ^ i) & ~num2
            num2 = (num2 ^ i) & ~num1

        return num1