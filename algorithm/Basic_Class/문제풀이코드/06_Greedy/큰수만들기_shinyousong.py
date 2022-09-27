# 실패 코드, 어떻게 할지 몰라서 일단 해봤음
def solution(number, k):
    # k번 반복
    i = 0
    while i < k:
        # 이전 숫자
        before = number[0]
        # 이전 숫자가 반복될 때, 그 길이(시간 줄이기)
        beforelen = 0
        for j in range(1, len(number)):
            # 앞보다 뒤가 더 큰 경우 앞을 그 길이만큼 제거
            if before < number[j]:
                # 다 제거 가능할 때
                if i + beforelen < k:
                    number = number[:j - (1 + beforelen)] + number[j:]
                    i += beforelen
                # 다 제거 불가능할 때
                else:
                    number = number[:j - (k - i)] + number[j:]
                    i = k
                break
            # 길어질 때
            elif before == number[j]:
                beforelen += 1
            # 초기화될 때
            elif before != number[j]:
                beforelen = 0
            # 반복이 의미 없는 경우
            if j + 1 == len(number):
                return number[:len(number) - (k - i)]
            before = number[j]
        i += 1
    return number
