def solution(answers):
    # 각 학생들의 정답 패턴 리스트 만들기
    st_one = [1, 2, 3, 4, 5]
    st_two = [2, 1, 2, 3, 2, 4, 2, 5]
    st_three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    # 첫 번째, 두 번째, 세 번째 학생들의 정답 개수를 담을 리스트
    cnt = [0,0,0]
   
    # 정답 개수만큼 for문을 돌면서 각 학생의 패턴과 비교
    for idx in range(len(answers)):
        tmp = answers[idx]
        # st_one
        if tmp == st_one[idx % 5]:
            cnt[0] += 1
        # st_two
        if tmp == st_two[idx % 8]:
            cnt[1] += 1
        # st_three
        if tmp == st_three[idx % 10]:
            cnt[2] += 1
   
    # 가장 많이 맞춘 횟수 저장
    tmp = max(cnt)
    # 가장 많이 맞춘 횟수의 인덱스를 추출
    return [i+1 for i, j in enumerate(cnt) if j == tmp]
