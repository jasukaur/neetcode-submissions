class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''

        for s in strs:
            encoded += str(len(s)) + '#' + s
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:

        decoded = []
        i = j = 0

        while j< len(s):
            if s[j] != '#':
                j +=1
            elif s[j] == '#':
                l = int(s[i:j])
                i = j+1
                decoded.append(s[i:i+l])
                i = i+l
                j = i
        return decoded
