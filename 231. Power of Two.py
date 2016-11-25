class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return bin(n).replace('0', '') == 'b1' and bin(n).startswith('0b1')
