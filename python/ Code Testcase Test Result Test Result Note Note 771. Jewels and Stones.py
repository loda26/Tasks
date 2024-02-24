class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        sum = 0
        for i in stones:
            if i in jewels:
                sum = sum + 1
        
        return sum
