class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            # Shift to the right by i
            bit = (n >> i) & 1
            # bit shift to the left by 31 - i
            res = res | (bit << (31 - i))

        return res        