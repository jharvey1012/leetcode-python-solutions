class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        globalMaximum = float('-inf')
        localMaximum = 0
        
        for number in nums:
            localMaximum  = max(localMaximum + number, number)
            globalMaximum = max(localMaximum, globalMaximum)
        return globalMaximum