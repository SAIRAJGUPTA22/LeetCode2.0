class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        first_str = strs[0]
        last_str = strs[-1]
        common =""
        for i in range(len(first_str)):
            if first_str[i] == last_str[i]:
                common += first_str[i]
            else:
                break
        return common