class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"
        
        num1, num2 = num1[::-1], num2[::-1]
        result = [0] * (len(num1) + len(num2))

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                result[i1 + i2] += digit
                result[i1 + i2 + 1] += result[i1 + i2] // 10
                result[i1 + i2] %= 10
        
        # Remove the leading zeros
        while len(result) > 1 and result[-1] == 0:
            result.pop()
        
        return "".join(str(digit) for digit in reversed(result))

        