def solution(n, lost, reserve):
    # 중복 제거
    reserve_copy = reserve.copy()
    for r in reserve:
        if r in lost:
            reserve_copy.remove(r)
            lost.remove(r)
    
    # 일단 기본: 전체에서 잃어버린 애 빼고
    answer = n - len(lost)
    
    # 잃어버린 애 sort - assert로 sort 안 된 경우 있는 거 확인함
    lost.sort()
    
    # reserve에서 pop하기 싫어서 check list 만듦
    # 학생 번호가 1부터 시작해서 0 추가 / lost에 중복으로 있는 경우 제외
    chk = [i in reserve_copy for i in range(n+1)]
    for l in lost:
        # 양쪽 끝에서 index에러 나는 경우 처리 해주기 위해 try-except 사용
        try:
            if chk[l - 1]:
                answer += 1
                chk[l - 1] = False
            elif chk[l + 1]:
                answer += 1
                chk[l + 1] = False
        except:
            continue
    
    return answer
