class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        max_count=0
        left=0

        seen = set()
        for right in range(len(s)):
            
            while s[right] in seen:
                seen.remove(s[left])
                left+=1
                count-=1

            seen.add(s[right])
            count+=1
            max_count= max(count,max_count)
        return max_count
        