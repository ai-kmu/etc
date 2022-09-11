def solution(brown, yellow):
    for i in range(1, int(brown/2)+2):
        col = i
        row = int(brown/2)+2-i
        if (row-2)*(col-2) == yellow:
            return [row, col]
        
