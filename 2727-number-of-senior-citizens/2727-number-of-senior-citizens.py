class Solution(object):
    def countSeniors(self, details):
        i = 0
        for p in details:
            if int(p[11:13]) > 60:
                i += 1
        return i
        """
        :type details: List[str]
        :rtype: int
        """
        