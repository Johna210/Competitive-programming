class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # string = "".join(map(str,digits))
        # number = int(string) + 1

        # value = []
        # for i in str(number):
        #     value.append(int(i))

        # return value
        carry = 0

        if digits[-1] <= 8:
            digits[-1] += 1
        
        else:
            carry = 1
            for i in range(len(digits)-1,-1,-1):
                val = (digits[i] + carry)
                carry = val // 10
                val = val % 10

                digits[i] = val
        
        if carry != 0:
            return [carry] + digits
        else:
            return digits

