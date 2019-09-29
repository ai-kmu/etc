def palindrome(start,i,s):
    for j in range(start,i):
        if s[j] != s[(i-j)+i]:
            return False
    return True

def solution(s):
    answer = 0
    
    for i in range(1,len(s)-1):
        if(i<len(s)/2):
            for start in range(0, i):
                if palindrome(start,i,s):
                    answer = max((i-start)*2 +1, answer)     
        else:
            for start in range(i-(len(s)-i)+1, i):
                if palindrome(start,i,s):
                    answer = max((i-start)*2 +1, answer)
                    

    return answer
