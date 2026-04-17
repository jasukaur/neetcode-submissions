class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ct = {}
        res = 0
        l, maxf = 0, 0

        for r in range(len(s)):
            ct[s[r]] = 1+ ct.get(s[r], 0)
            maxf = max(maxf, ct[s[r]])

            while (r-l+1) - maxf > k:
                ct[s[l]] -= 1
                l +=1
            res = max(res, r-l+1)
        return res


            