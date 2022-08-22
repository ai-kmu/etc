# 왜 time limit error가 뜨는지 잘 모르겠어요..ㅠㅠ
def solution(n, t, m, p):
    answer = ''
    game = ''
    num = 0
    
    while len(game) < t * m:
        # 몇진법이냐에 따라서 진법 변환 내장함수를 다르게 호출
        if n == 2:
            # slicing 한 이유는 0b가 붙은 채로 str이 return 되기 때문
            game += bin(num)[2:]
        
        if n == 8:
            game += oct(num)[2:]
        
        if n == 16:
            game += hex(num)[2:]
            
        num += 1

    p = p - 1
    game = game.upper()
    
    # t 길이만큼 while 문을 돌고
    while len(answer) != t:
        # 튜브가 답해야 하는 숫자만 answer에 더해줌
        answer += game[p]   
        p += m
    
    return answer
