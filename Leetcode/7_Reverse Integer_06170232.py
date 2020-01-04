class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            x = str(x)
            x = x[::-1]
            x = int(x)
        elif x < 0:
            x = str(-x)
            x = x[::-1]
            x = int(x)
            x = -x
        if x.bit_length() < 32:
            return x
        else:
            return 0
