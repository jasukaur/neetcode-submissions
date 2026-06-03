class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l, r = 0 , 0
        maxLength = 0

        while r < len(s):
            if s[r] not in charSet:
                maxLength = max(maxLength, r-l+1)
            else:
                while s[l] != s[r]:
                    charSet.remove(s[l])
                    l += 1
                    
                l +=1

            charSet.add(s[r])
            r += 1
        return maxLength

