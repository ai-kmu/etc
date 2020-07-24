# Longest Substring Without Repeating Characters
# 2:40~ 3:10
class Solution(object):
    def lengthOfLongestSubstring(self, s):

        substring=[] # substring을 저장할 변수
        max_length=0
        for char in s:
            if not char in substring:
                substring.append(char)
            else: # 만약 substring에 들어있는 글자가 또 들어오면 substring 끝난 것
                current_length=len(substring)
                if max_length<current_length:  #지금까지의 제일 긴 substring보다 현재 substring이 더 길다면 갱신
                    max_length=current_length

                char_index=substring.index(char)
                substring=substring[char_index+1:] # substring을 갱신할 때 중복된 char이후부터는 그대로 둠
                substring.append(char)


        if max_length<len(substring): #마지막에 다시 max_length 계산하기
            max_length=len(substring)

        return max_length

if __name__ == '__main__':
    input="dvdf"
    s=Solution()
    print(s.lengthOfLongestSubstring(input))



