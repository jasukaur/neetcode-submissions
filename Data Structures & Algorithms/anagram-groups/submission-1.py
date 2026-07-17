class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}

        for s in strs:
            cs = tuple(sorted(s))

            if cs in hm:
                hm[cs].append(s)
            else:
                hm[cs] = [s]
        return list(hm.values())