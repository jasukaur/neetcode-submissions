class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = {}
        l = 0
        maxF = 0
        longest = 0

        for r in range(len(s)):
            hm[s[r]] = 1 + hm.get(s[r], 0)
            maxF = max(maxF, hm[s[r]])

            while (r-l+1) - maxF > k:
                hm[s[l]] -= 1
                l +=1
            longest = max(longest, r-l+1)
        return longest