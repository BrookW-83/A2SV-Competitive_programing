class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}

        def dp(index1, index2):
            if index1 == len(nums1) or index2 == len(nums2):
                return 0

            if (index1, index2 )in memo:
                return memo[(index1, index2)] 

            connect = 0

            if nums2[index2] == nums1[index1]:
                connect += max(1+ dp(index1 + 1, index2+1),  dp(index1+1, index2))

            else:
                connect += max(dp(index1+1, index2), dp(index1, index2+1))

            memo[(index1,index2)] = connect

            return connect


        return dp(0, 0)
