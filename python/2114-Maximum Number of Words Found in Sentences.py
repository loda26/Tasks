class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        result = 0

        for words in sentences:
            tmp = len(words.split(" "))
            if tmp > result:
                result = tmp

        return result
