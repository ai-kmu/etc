'''
1. 0부터 목표까지 문자열 리스트, total 생성
2. total[::(p-1)]이 답임
* n진수 변환을 위한 함수 정의 필요
'''

# 10진수 num을 base진수로 변환하기 위한 함수
# 123(n) = n * n * 1 + n * 2 + 3
#        = n * (n * (1) + 2) + 3 임을 이용함
def convert(num, base):
    temp = '0123456789ABCDEF'
    q, r = divmod(num, base)
    
    if q:
        return convert(q, base) + temp[r]
    else:
        return temp[r]

def solution(n, t, m, p):
    answer = ''
    
    # t * m개 만들기
    i = 0
    while len(answer) < t * m:
        answer += str(convert(i, n))
        i += 1
    
    # 하지만 만들고 나면 t * m보다 좀 더 길어질 수 있으니 자르기
    # ex) 테케1번: 0 1 10 11 100
    # 11까지 8개 안 돼서 100을 더하는 순간 8개보다 많아짐
    answer = answer[:t*m]
    
    # python index로 변환: 1번째 = 0
    p -= 1
    
    # p번째에서 시작해서 m개 씩 건너뛰면서 갖고 오기
    return answer[p::m]
