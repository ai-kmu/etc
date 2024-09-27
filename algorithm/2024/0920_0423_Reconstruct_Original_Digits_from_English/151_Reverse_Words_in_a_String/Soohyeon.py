class Solution(object):
    def reverseWords(self, s):
        
        words = s.split()
        len_x = len(words)
        result = ""

        for x in range(len_x):
            index = words[len_x - 1 - x]
            if x == len_x -1 :
                result += index
            else:
                result += index + " "

        return result

        