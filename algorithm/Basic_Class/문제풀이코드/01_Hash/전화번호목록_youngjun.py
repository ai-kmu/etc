#solution 1. starswith 사용

def solution(phone_book):
    phone_book.sort(key = len)
    for i in range(len(phone_book)):
        for j in phone_book[i+1:]:
            if j.startswith(phone_book[i]):
                return False
    return True
