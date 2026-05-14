class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        i = 0
        sign = 1
        ans = 0
        while i<len(s) and s[i]==" ":
            i+=1
        
        if i == len(s):
            return 0
        
        if s[i] == "-":
            sign = -1
            i += 1
        elif s[i] == "+":
            i+=1

        while i<len(s) and s[i].isdigit():
            ans = ans*10 + int(s[i])

            # Clamp to 32-bit signed integer range
            if sign * ans > 2**31 - 1:
                return 2**31 - 1
            if sign * ans < -2**31:
                return -2**31
            i+=1

        return ans*sign