class Solution:
    #kadane's algorithm
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currentSum = float('-inf'), 0
        
        for n in nums: 
            #Which is better, adding the next number to the current sum or just taking the next number?
            currentSum = max(currentSum+n, n) 
            # Which is better, keeping our max sum we've found before or using our new current sum?
            maxSum = max(maxSum, currentSum)
            
        return maxSum