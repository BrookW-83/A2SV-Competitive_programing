class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pointer1, pointer2 = m, 0

        while pointer1 <= len(nums1)-1:
            if nums1[pointer1] == 0:
                nums1[pointer1] = nums2[pointer2]
                pointer1 += 1
                pointer2 += 1
        nums1.sort()
                    
        print(nums1)


        