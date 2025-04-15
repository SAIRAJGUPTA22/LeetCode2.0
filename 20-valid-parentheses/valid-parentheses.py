class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack =[]
        bracket_map ={')':'(',']':'[','}':'{'}
        for char in s:
            if char in bracket_map:
                if not stack or stack.pop() !=bracket_map[char]:
                    return False
            else:
                stack.append(char)
        return not stack
        