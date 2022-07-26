def solution(phone_book):
    hash_dict = {}
    
    for phone_num in phone_book:
        hash_dict[phone_num] = 1
    
    # temp에 i를 하나씩 추가하면서 if 조건 만족하는지 확인. 만족 : False
    for phone_num in phone_book:
        temp = ""
        for i in phone_num:
            temp += i
            if temp in hash_dict and temp != phone_num:
                return False
    return True
