def solution(s):
    for i in range(len(s),0,-1):
        for k in range(len(s)-i+1):
            j=s[k:k+i]
            if (j==j[::-1]):
                return i
