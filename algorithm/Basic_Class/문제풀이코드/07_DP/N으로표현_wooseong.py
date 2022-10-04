def solution(N, number):
    DP = []
    # ns: 반복 횟수
    for ns in range(1, 9):
        # 제일 처음으로 가능한 값은 NN..N
        cand = set()
        repeat = int(str(N) * ns)
        cand.add(repeat)
        
        for j in range(ns - 1):
            # 연산자 왼쪽
            for op1 in DP[j]:
                # 연산자 오른쪽
                for op2 in DP[-j-1]:
                    # 사칙연산 결과 추가
                    cand.add(op1 + op2)
                    cand.add(op1 - op2)
                    cand.add(op1 * op2)
                    # divide by zero 피하기
                    if op2 != 0:
                        cand.add(op1 // op2)
        
        # target number가 생겼으면
        # ns가 최솟값임
        if number in cand:
            answer = ns
            break
        
        # N을 ns번 사용했을 때 결과들을 DP[ns - 1]에 저장
        DP.append(cand)

    # for 문을 멀쩡히 다 돌았다 == break 안했다 == target number 없다 == 8번 안에 불가능
    else:
        answer = -1
    
    return answer
