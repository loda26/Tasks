class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hay = len(haystack)
        ned = len(needle)

        for i in range(hay):
            if haystack[i: i + ned] == needle:
                return i
        
        return -1
