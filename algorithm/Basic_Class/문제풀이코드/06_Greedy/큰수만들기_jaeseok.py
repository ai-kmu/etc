# 테스트케이스 12번 통과못함
def solution(number, k):
    number = list(number)
    numlist = []
    for i in range(len(number)):
        # numlist가 비어있지 않고 아직 뺄 숫자가 남았고 뒤 자리수가 앞보다 크면
        # 그 수를 제거하고 k에 1을 뺌
        while numlist and k > 0 and numlist[-1] < number[i]:
            numlist.pop()
            k -= 1
        # k가 0이 되면 number에서 남은 수를 붙여주고 loop를 빠져나감
        if k == 0:
            numlist += number[i:]
            break
        # numlist에 숫자를 한 자리씩 계속 붙여나감
        numlist.append(number[i])
    
    answer = ''.join(numlist)
    return answer
