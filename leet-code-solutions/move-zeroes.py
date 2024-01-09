class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p =0
        c =0
               
        while c < len(nums):
            if nums[c] != 0:
                nums[p], nums[c]= nums[c], nums[p]
                p +=1
            
            c+=1
           
            
        
        
        
        