# solution 1. 
def longest_palindrom(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            if(s[j:j+i] == s[j:j+i][::-1]):
                return i




# solution 2. run time error 
def longest_panlindrom2(s):
    pan_length = []
    table = []
    
    for i in range(0, len(s)):
        for j in range(1, len(s)+1):
            if s[i:j] == (s[i:j])[::-1]:
                pan_length.append(len(s[i:j]))
                
    return max(pan_length)


# solution 3. run time error
def longest_panlindrom3(s):

    table = [[False, False, False, False, False, False, False] for i in range(7)]

    for i in range(len(s)):
        table[i][i] = True
        answer = 1
        
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            table[i][i+1] = True
            answer = 2
            
            
    for i in range(3, len(s) + 1):
        k = 0
        for j in range(len(s) - i + 1):
            k = i + j - 1
            if table[j+1][k-1] and (s[j] == s[k]):
                table[j][k] = True
                if i > answer:
                    print(i)
                    answer = i

    return answer
