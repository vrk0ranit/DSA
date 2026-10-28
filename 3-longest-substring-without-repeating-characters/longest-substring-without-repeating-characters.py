class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        seen={}
        max_l=0
        for r in range(len(s)):
            char=s[r]
            if char in seen and seen[char]>=l:
                l=seen[char]+1
            seen[char]=r
            max_l=max(max_l,r-l+1)    
        return max_l