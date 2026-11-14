class Solution:
    def maxSubarraySum(self, arr):
        # Code here
        res=arr[0]
        maxsum=arr[0]
        for i in range(1,len(arr)):
            maxsum=max(arr[i],maxsum+arr[i])
            res=max(res,maxsum)
        return res
'''
Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray [7, -1, 2, 3] has the largest sum 11.
O(1)
'''
