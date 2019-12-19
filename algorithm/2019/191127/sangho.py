from collections import deque as queue

# 단어 한개 차이면 T , 아니면 F
def comparison(a,b):
    cmp = zip(a,b)
    count = 0
    for x,y in cmp:
        if x != y :
            count += 1
    if count == 1:
        return True
    return False

def solution(begin,target,words):
    if target not in words:
        return 0
    
    q, dic = queue(), dict()
    q.append((begin, 0))
    
    # 단어 하나차이걸 set에 저장
    set_1 = set()
    for i in words:
        if (comparison(i,begin)):
            set_1.add(i)
    dic[begin] = set_1
    
    # words 끼리 단어하나 차아나는걸 구해둠
    for w in words:
        set_2 = set()
        for i in words:
            if (comparison(i,w)):
                set_2.add(i)
        dic[w] = set_2
    
    # 탐색
    while q:
        word, level  = q.popleft()
        for dc in dic[word]:
            if dc == target:
                return level + 1
            else:
                q.append((dc, level + 1))
    
    return 0