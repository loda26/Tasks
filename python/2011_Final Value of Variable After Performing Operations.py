class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        result = 0

        for op in operations:
            if op == "--X" or op == "X--":
                result = result - 1
            if op == "X++" or op == "++X":
                result = result + 1

        return result
