class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        targetSum = {}

        for i in range(len(nums)):
            currdiff = target - nums[i]

            if currdiff in targetSum:
                return [targetSum[currdiff], i]

            else:
                targetSum[nums[i]] = i

                

        