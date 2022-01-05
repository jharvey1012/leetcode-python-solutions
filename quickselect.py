# Quickselect
class Solution:
	def findKthLargest(self, nums: List[int], k:int) -> int:
		# Very important we do this instead of just using the pivot. Because what if there are multiple instances of the pivot element
        pivot = random.choice(nums)
        numbersEqualToPivot     = [x for x in nums if x == pivot]
        numbersGreaterThanPivot = [x for x in nums if x > pivot]
        numbersLessThanPivot    = [x for x in nums if x < pivot]
        numElmsGreaterThanPivot = len(numbersGreaterThanPivot)
        numElmsInMid            = len(numbersEqualToPivot)
                
            
        # Let's say there are 3 elms greater than pivot and we're looking for the 4th largest, it wouldn't be in         the "numbersGreaterThanPivot" arr if there are only 3 elmns in there            
        if k <= numElmsGreaterThanPivot: 
            return self.findKthLargest(numbersGreaterThanPivot, k)
        # So if k is greater than the number of elements larger than the pivot (and the midpoint),
        # look in the array of numbers smaller than the pivot....Offset k by the number of elements on the 
        # other half of the array, as those will be the "k largest" already.
        elif k > (numElmsGreaterThanPivot + numElmsInMid):
            return self.findKthLargest(numbersLessThanPivot, k - (numElmsGreaterThanPivot + numElmsInMid))
        # Remember the pivot always end up in its sorted position after quicksort. So if k is the pivot,
        # then we know it's in the sorted order (kth largest)
        else: 
            return pivot