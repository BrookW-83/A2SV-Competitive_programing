class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        oddCount, evenCount = defaultdict(int), defaultdict(int)

        for i in range(len(nums)):
            if i % 2 == 0:
                evenCount[nums[i]] += 1

            else:
                oddCount[nums[i]] += 1


        topOdd, secondOdd = (None, 0), (None, 0)
        for num in oddCount:
            if topOdd[1] < oddCount[num]:
                topOdd, secondOdd = (num, oddCount[num]), topOdd

            elif secondOdd[1] < oddCount[num]:
                secondOdd = (num, oddCount[num])

        topEven, secondEven = (None, 0), (None, 0)
        for num in evenCount:
            if topEven[1] < evenCount[num]:
                topEven, secondEven = (num, evenCount[num]), topEven

            elif secondEven[1] < evenCount[num]:
                secondEven = (num, evenCount[num])


        if topOdd[0] != topEven[0]:
            return len(nums) - (topOdd[1] + topEven[1])
        else:
            return len(nums) - max(topOdd[1] + secondEven[1], topEven[1] + secondOdd[1])

        
                
        
