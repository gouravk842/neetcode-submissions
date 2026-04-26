class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        [0 1 0 2 3 0]
        """


        start =0
        end=0
        for start in range(0,len(nums)):
            if nums[start]!=0:
                nums[start],nums[end]=nums[end],nums[start]
                end+=1
                

        