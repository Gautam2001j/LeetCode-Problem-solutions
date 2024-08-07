class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        count =0
        temp = x
        while temp != 0:
            a = temp%10
            count = count*10+a
            temp /= 10
        return count == x

        """
        :type x: int
        :rtype: bool
        """
        