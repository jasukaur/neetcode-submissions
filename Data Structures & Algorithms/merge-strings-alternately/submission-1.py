class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ''
        i, j = 0, 0
        w1L = len(word1)
        w2L = len(word2)

        while i < w1L and j < w2L:
            ans += (word1[i])
            ans += (word2[j])
            i += 1
            j += 1
        
        if i< w1L:
            ans += (word1[i:w1L])
        if j< w2L:
            ans += (word2[j:w2L])
        return ans
        
        