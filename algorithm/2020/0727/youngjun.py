# Longest Substring Without Repeating Characters
# 2:40~ 3:10
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        substring=[]
        max_length=0
        for char in s:
            if not char in substring:
                substring.append(char)
            else:
                current_length=len(substring)
                if max_length<current_length:
                    max_length=current_length

                char_index=substring.index(char)
                substring=substring[char_index+1:]
                substring.append(char)


        if max_length<len(substring):
            max_length=len(substring)

        return max_length

if __name__ == '__main__':
    input="dvdf"
    s=Solution()
    print(s.lengthOfLongestSubstring(input))



