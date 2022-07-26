def solution(str1, str2):
    multi_str1 = []
    multi_str2 = []
    both = {}
    both_str1 = {}
    both_str2 = {}
    gyo = 0   
    
    # 글자쌍만들기
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            multi_str1.append(str1[i:i+2].lower())
    for j in range(len(str2)-1):
        if str2[j:j+2].isalpha():
            multi_str2.append(str2[j:j+2].lower())
    
    # trivial case
    if not multi_str1 and not multi_str2:
        return 65536
    
    # 교집합 체크 for문
    for m_str1 in multi_str1:
        for m_str2 in multi_str2:
            if m_str1 == m_str2:
                # 교집합 요소 저장
                both[m_str1] = m_str2
    
    # 각 str 별 교집합 요소별 개수 count -> min을 통해 교집합 수 gyo 구하기 위해
    for char in both:
        both_str1[char] = multi_str1.count(char)
        both_str2[char] = multi_str2.count(char)
    
    # 최종 교집합 수 count
    for i in both:
        gyo += (min(both_str1[i], both_str2[i]))
    
    # 교집합 / ([집합A+집합B-교집합] == 합집합)
    J = gyo / (len(multi_str1) + len(multi_str2) - gyo)

    return int(J*65536)
