def solution(phone_book):
    answer = True
    
    a = {i for i in phone_book}
    
    for phone_num in phone_book:
        temp = ""
        for num in phone_num:
            temp += num
            if temp in a and temp != phone_num:
                answer = False
    
    return answer
