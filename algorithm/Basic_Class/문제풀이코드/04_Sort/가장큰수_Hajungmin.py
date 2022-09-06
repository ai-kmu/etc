# 테스트 케이스 1만 통과
# 개선 필요

def solution(numbers):
    # numbers에 있는 숫자들을 1000의 자리에 맞춰준다음 내림차순으로 정렬
    # 이후 string으로 변환해서 join을 통해 정답값 만들기
    nums = sorted(numbers, key=lambda x: str(x + 10*x + 100*x), reverse=True)
    nums = list(map(str, nums))
    
    return ''.join(nums)
