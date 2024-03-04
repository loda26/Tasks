class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        tmp = ""
        output = []

        for i in digits:
            tmp += str(i)
        
        int_result = int(tmp) + 1
        str_result = str(int_result)

        for i in str_result:
            output.append(int(i))

        return output
