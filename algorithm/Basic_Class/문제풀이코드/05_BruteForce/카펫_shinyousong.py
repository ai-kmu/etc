def solution(brown, yellow):
    # 가로의 길이가 더 길게, 1부터 사각형의 둘레/2+1까지 돌면서 조합을 계산한다.
    for i in range(1, int(brown/2)+2):
        col = i
        row = int(brown/2)+2-i
        # 사각형 내부 넓이가 yellow가 될 때 리턴
        if (row-2)*(col-2) == yellow:
            return [row, col]
        
