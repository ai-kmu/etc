def solution(number, k):
    answer = ''
    max_length = len(number) - k     # 최대 자릿수
    
    start = 0                        # 검색 시작할 인덱스
    for i in range(max_length):      # 자릿수만큼 검색
        max_num = number[start]      
        max_idx = start
        for j in range(start,k+i+1): # 자릿수에서 가장 큰 값 구하기
            if max_num < number[j]:
                max_num = number[j]
                max_idx = j
        start = max_idx + 1          # 가장 큰 값 더해주기
        answer += max_num
    return answer
