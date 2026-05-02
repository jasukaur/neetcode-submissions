class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        output = []
        carry = 1

        for i in range(len(digits)-1, -1, -1):
            curr = digits[i] + carry
            if curr > 9:
                carry = 1
                curr = 0
            else:
                carry = 0
            output.append(curr)
        
        if carry:
            output.append(1)
        print(output)
        return output[::-1]