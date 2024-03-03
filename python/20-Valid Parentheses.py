class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in s:
            if s[i] == "(":
                if s[i+1] != ")":
                    return False
            if s[i] == "{":
                if s[i+1] != "}":
                    return False
            if s[i] == "[":
                if s[i+1] != "]":
                    return False
        
        return True
