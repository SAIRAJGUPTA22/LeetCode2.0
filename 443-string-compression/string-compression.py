class Solution:
    def compress(self, chars: List[str]) -> int:
        i=0
        j=0
        while i < len(chars):
            letter = chars[i]
            c = 0
            while i < len(chars) and chars[i] == letter:
                c = c+1
                i=i+1
            chars[j] = letter
            j = j+1
            if c>1:
                for c in str(c):
                    chars[j]=c
                    j = j+1
        return j
            
        