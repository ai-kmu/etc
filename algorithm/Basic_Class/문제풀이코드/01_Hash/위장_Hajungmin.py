def solution(clothes):
    cloth_dict = dict()
    
    # 옷의 종류와 그 개수를 딕셔너리로 만든다
    # 각 종류에 몇 개의 옷이 있는지 개수를 센다
    for i in clothes:
        if i[1] not in cloth_dict:
            cloth_dict[i[1]] = 1
        else:
            cloth_dict[i[1]] += 1
            
    ans = 1
    # 딕셔너리를 돌며 옷을 입는 가지 수를 구한다
    # 현재 경우의 수 * (현재 각 옷 종류의 개수 + 1(안입는 경우))
    for i in cloth_dict:
        ans *= cloth_dict[i] + 1
    
    # 꼭 하나의 옷은 입는다고 했으므로 결과에서 1을 빼준다
    return ans - 1
