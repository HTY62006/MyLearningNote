class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num%4 == 0 and num>1:
            num/=4
        if num == 1:
            return True
        else:
            return False
