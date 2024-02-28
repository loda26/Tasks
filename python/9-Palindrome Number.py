class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev_num = 0
        num = x

        while num:
            rev_num *= 10
            rev_num += num % 10
            num /= 10
        
        return rev_num == x
