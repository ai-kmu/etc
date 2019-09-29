def solution(s):
    re_s = s[::-1]
    #팰린드롬이 가능한 단어들을 담을 리스트
    lst1 = list()
    #팰린드롬일 경우 담을 세트/ 겹치는걸 없게 하기 위해서 세트로 생성
    lst2 = set()
    for i in range(len(re_s)):
        for k in range(i, len(re_s)):
            lst1.append(re_s[i:k+1])
        for w in lst1:
            if w == w[::-1]:  lst2.add(len(w))
        lst1 = list()
    return max(lst2)
