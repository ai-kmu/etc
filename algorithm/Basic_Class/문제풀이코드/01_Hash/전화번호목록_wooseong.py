def solution(phone_book):
    # 각 전화번호의 길이 저장
    len_set = set(len(i) for i in phone_book)
    # 모든 전화번호의 길이에 맞게 각 전화번호 잘라두기 (hash)
    # 전화번호: set(자른 것들)
    # set으로 하는 이유: 해당 전화번호의 길이보다 긴 걸로 자르면 다 똑같은 게 나와서
    part_dict = {i:set(i[:j] for j in len_set) for i in phone_book}
    
    # 각 전화번호에 대해서
    for phone_num in phone_book:
        # 자른 것들 들고와서
        part = part_dict[phone_num]
        for prefix in part:
            # 걔들 중 하나라도 자기 자신 제외하고 원래 전화번호랑 같은 게 있다면
            if (prefix != phone_num) and (prefix in part_dict):
                # 중복임. False
                return False
    
    # for문을 return 없이 다 돌았다 = 중복 없음. True
    return True
