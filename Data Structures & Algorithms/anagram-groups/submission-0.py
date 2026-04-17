class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for i in strs:
            k = tuple(sorted(i))

            if k not in hm:
                hm[k] = [i]
            else:
                hm[k].append(i)
        
        return list(hm.values())