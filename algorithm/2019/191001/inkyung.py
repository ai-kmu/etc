def solution(operations):
    answer = []
    #operations안의 연산을 수행할 리스트
    lst = []
    maxN, minN = 0, 0
    for i in operations:
        if i[0] == "I": 
            lst.append(float(i[2:]))
            maxN, minN = max(lst), min(lst)
            continue
        try:
            if i == "D 1":  
                lst.remove(maxN)
                maxN = max(lst)
            elif i == "D -1":   
                lst.remove(minN)
                minN = min(lst)
        except:
            continue
    if not lst: answer = [0, 0]   
    else: 
        answer.append(max(lst))
        answer.append(min(lst))
