class Solution:
    def search(self, nums: List[int], target: int, offset = 0) -> int:
        # In the case of an empty array, just return -1
        if len(nums) == 0: return -1
        if len(nums) == 1 and nums[0] == target: return 0
        elif len(nums) == 1 and nums[0] != target: return -1
        
        # If the numbers are sorted, we have take the middle number
        # if the middle number is what we're looking for, we're done.
        midPointIndex = len(nums) // 2
        pivot = nums[midPointIndex]
        
        # If the middle number is greater than what we're looking for, we kmow the number
        # is on the left-side of the 'pivot', so throw away the right half side
        # if the middle number is lower, we know what we're looking for is on the right side of
        # the pivot, so throw away the left-half
        
        # Rinse, repeat
        # each time we only continue with half of the original size of the array.
        # we can split an array by 2 log(n) times, thus the complexity is O(log(n))
        if pivot == target:
            return midPointIndex + offset # we use an offset because if we "throw away" elements we need to know how we're affecting array indexing
        elif pivot > target:
            return self.search(nums[:midPointIndex], target, offset)
        else:
            return self.search(nums[midPointIndex:], target, len(nums[:midPointIndex]) + offset)
    
        
