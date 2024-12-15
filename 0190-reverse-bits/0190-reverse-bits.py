class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0 
        for i in range(32):
            bits = (n>>i) & 1
            result = result | (bits << (31-i))
        return result
        