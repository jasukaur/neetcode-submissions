class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dup = set()
        l, r = 0, 0
        maxLen = 0

        while r < len(s):
            if s[r] in dup:
                while s[l] != s[r]:
                    dup.remove(s[l])
                    l+=1
                dup.remove(s[l])
                l += 1
            dup.add(s[r])
            maxLen= max(maxLen, len(dup))
            r +=1
        return maxLen





