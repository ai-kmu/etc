def palindrome_check(n): # palindrome 이면 true, 아니면 false
    a = len(n) // 2
    if n[a:] ==  n[::-1][a:]:
        return True
    return False
    
def solution(s):
    answer = 0 
    for i in range(0,len(s)):
        for j in range(1,len(s)+1-i):
            text = s[i:i+j]
            if palindrome_cheak(text) :
                if len(text) > answer :
                    answer = len(text)
    return answer