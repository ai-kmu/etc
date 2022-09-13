from itertools import permutations

def solution(numbers):
    
    # 소수 판별
    # 2보다 작거나 자신을 반으로 나눈 수까지 나눠지면 소수가 아님
    def isprime(num):
        if num < 2:
            return False
        for i in range(2, int(num)//2 + 1):
            if num % i == 0:
                return False
        else:
            return True
    
    
    nums = set()
    answer = 0
    # 순열을 통해 집합에 가능한 숫자들을 저장
    for i in range(len(numbers)):
        for j in list(permutations(numbers, i + 1)):
            nums.add(int("".join(j)))
    # 집합의 원소 각각의 소수를 
    for num in nums:
        if isprime(num):
            answer += 1
    return answer
