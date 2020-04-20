"""
스스로 코딩 해본 것이 잘 안돼서, 다른 사람 아이디어 참조 후 다시 코딩한 코드. 
Point
    - def(A) 내부에 다시 def(B)을 사용함으로써, 전역변수나 함수(B)의 많은 매개변수 사용을 줄였다.
    - banned_id 원소 하나 당, 매핑이 되는 user_id 하나를 골라낸다.
"""

def solution(user_id, banned_id):
    
    def check(b_id, user):
        """
        하나의 user_id와 b_id를 비교한다. 
        user_id가 b_id에 속하는 것이라면, return True.
        아니라면, return False. 
        """
        for s in range(len(b_id)):
            if b_id[s] != '*':
                if b_id[s] != user[s]:
                    return False
            elif b_id[s] == '*':
                continue
        else:
            return True

    def back(u, b):
        if b == N2: # Reculsivd Function의 Base condition이다. "user_id 하나와 banned_id 모두를 다 비교했다면."
            if u not in result:
                result.append(u[:]) # u를 copy by value해서 result 에 넣는다. **중요**
            return
        for i in range(N1): # user_id의 원소를 하나씩 살펴본다. 
            # 위에서 고른 user_id의 하나와, banned_id의 원소 모두와 비교해본다.
            if u[i] == 0 and len(banned_id[b]) == len(user_id[i]): # 중요한 전제 조건. 2 문자열의 길이가 같아야 한다. 
                if check(banned_id[b], user_id[i]) == True: 
                    u[i] = 1
                    back(u, b + 1)
                    u[i] = 0

    # 1 : 변수 선언 및 정의
    answer = 0
    N1 = len(user_id)
    N2 = len(banned_id)
    u = [0 for ii in range(N1)]  # u[k]=1 는 user_id[k]가 banned_id 중 하나에 해당함을 의미한다. 
    result = [] # 가능한 u 배열의 경우와 수를 저장한다. 
    back(u, 0)
    answer = len(result) # 입출력 예 1의 result = [[1,0,0,1,0] , [0,1,0,1,0]]. 즉 2가지 경우가 존재한다.
    return answer
