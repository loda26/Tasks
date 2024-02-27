class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        sep = ''
        test_word1 = sep.join(word1)
        test_word2 = sep.join(word2)

        return test_word1 == test_word2
