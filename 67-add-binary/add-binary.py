class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result =''
        carry =0
        i,j = len(a)-1,len(b)-1
        while i>=0 or j>=0 or carry:
            total = carry
            if i>=0:
                total = total+int(a[i])
                i -= 1
            if j>=0:
                total = total+int(b[j])
                j -= 1
            result = str(total%2)+result
            carry = total//2
        return result
        