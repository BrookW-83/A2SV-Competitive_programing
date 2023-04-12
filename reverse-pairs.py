class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0

        def divide(nums):

            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            left_half = divide(nums[:mid])
            right_half= divide(nums[mid:])
            
            return merge(left_half, right_half)


        def merge(left_half, right_half):
            arr = []
            l, r = 0, 0

            nonlocal count
            while l < len(left_half) and r < len(right_half):
                if left_half[l] > 2 * right_half[r]:
                    l += 1
                    count += len(right_half) - r

                else:
                    r += 1

            i , j = 0, 0
            while i < len(left_half) and j < len(right_half):

                if left_half[i] > right_half[j]:
                    arr.append(left_half[i])
                    i += 1

                else:
                    arr.append(right_half[j])
                    j += 1
            arr.extend(left_half[i:])
            arr.extend(right_half[j:])

            return arr

        divide(nums)

        return count