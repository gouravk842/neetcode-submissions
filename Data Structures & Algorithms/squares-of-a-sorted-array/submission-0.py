class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Create a result array of the same length
        result = [0] * n
        
        # Pointers for the left and right ends of the input
        left = 0
        right = n - 1
        
        # Fill the result array from back to front
        for i in range(n - 1, -1, -1):
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] ** 2
                left += 1
            else:
                result[i] = nums[right] ** 2
                right -= 1
                
        return result
        