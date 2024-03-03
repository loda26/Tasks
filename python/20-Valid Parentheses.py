class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        brackets = {'(': ')', '{': "}", '[': ']'}

        for bracket in s:
            if bracket in brackets.keys():
                stack.append(bracket)
            else:
                if len(stack) == 0:
                    return False
                popped = stack.pop()
                if bracket == ')' and popped != '(':
                    return False
                elif bracket == '}' and popped != '{':
                    return False
                elif bracket == ']' and popped != '[':
                    return False
        
        return (len(stack) == 0)
