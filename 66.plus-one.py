class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        j = len(digits) - 1
        carry = 1
        while j >= 0:
            curr = (digits[j] + carry)
            carry = curr // 10
            digits[j] = curr % 10
            j -= 1
        if carry > 0:
            digits = [1] + digits
        return digits
