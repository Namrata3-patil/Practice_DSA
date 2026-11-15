class Solution:
    def productExceptSelf(self,nums: list[int]) -> list[int]:
        n = len(nums)
        result = [1] * n
    
    # Step 1: Calculate prefix products
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
    # Step 2: Multiply by suffix products
        right_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        return result
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
Input: nums = [1,2,3,4]
Output: [24,12,8,6]
O(n)
'''
