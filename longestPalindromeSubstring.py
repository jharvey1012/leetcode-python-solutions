class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l,r):
            # expand outward from center until we hit the bounds
            while (l >= 0 and r < len(s) and s[l] == s[r]):
             l -= 1
             r += 1
            return s[l+1:r]
        
        res = ""
        
        for i in range(len(s)): # for every character in the string
            # Expand outward from the center until you find characters that don't match
            test = helper(i,i) 
            # if we found a longer string than what we had before, set it
            if len(test) > len(res): res = test
            # Here we literally just do the same thing again starting from two characters next to each               other. It's ok if the string is even, because in that case it just won't return a length                 longer than the greatest palindrome we found above
            test = helper(i,i+1)
            if len(test) > len(res): res = test
                
        
        return res