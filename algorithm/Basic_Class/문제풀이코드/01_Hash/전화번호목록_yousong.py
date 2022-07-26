def solution(phone_book):
    dict = {}
    phone_book.sort(key = lambda x: len(x))
    for str1 in phone_book:
        dict[str1] = 0
        for i in range(len(str1)):
            if str1[:i] in dict:
                return False
    return True
