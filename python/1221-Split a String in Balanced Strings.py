class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        tmp = 0

        for i in s:
            if i == "L":
                tmp += 1
            else:
                tmp -=1
            if tmp == 0:
                result += 1

        return result
