class Solution:
  def longestPalindrome(s: str) -> str:
    max_length = 0
    start_index = 0

    start_index,max_length = 0, 0
    if len(s) == 1:
      return s

    elif len(s) == 0:
      return ""

    else:
      for i in range(len(s)):
        if s[i - max_length : i+1] == s[i - max_length:i+1][::-1]:
          start_index, max_length = i-max_length, max_length+1
        
        elif i-max_length > 0 and s[i-max_length-1: i+1] == s[i-max_length-1: i+1][::-1]:
          start_index, max_length = i-max_length-1, max_length+2

    return s[start_index: start_index+max_length]