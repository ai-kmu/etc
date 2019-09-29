
def isPalindrome(string):
    str_reverse = string[::-1]
    
    if(string == str_reverse):
        return True
    else:
        return False
    
    
def solution(s):
    answer = 0
    palindrome = []
    
    for i in range(len(s)):
        for j in range(1, len(s)+1):
            if(isPalindrome(s[i:j])):
                if(answer < len(s[i:j])):
                    answer = len(s[i:j])
                
    return answer