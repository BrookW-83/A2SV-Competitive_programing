class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        pattern = []
        min_val = nums[0]

        for num in nums:
            while pattern and num > pattern[-1][1]:
                pattern.pop()

            if pattern and num < pattern[-1][1] and num > pattern[-1][0]:
                return True

            pattern.append([min_val, num])
            min_val  = min(min_val, num)
      
        return False