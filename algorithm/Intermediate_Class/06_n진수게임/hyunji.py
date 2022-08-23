def solution(n, t, m, p):
    answer = ''
    game = ''
    
    # 진법 변환해주는 함수 (10 -> n 진법)
    def change_n(num):
        number = '0123456789ABCDEF'
        change = ''
        a, b = divmod(num, n)
        change += number[b]
        
        # 몫이 0이 될 때까지 계속 몫을 n으로 나눠준다
        while a != 0:
            a, b = divmod(a, n)
            # 나머지를 계속 더해준다
            change += number[b]
        
        # 문자열을 뒤집어줌
        return change[::-1]
        
    num = 0
    while len(game) < t * m:
        # change_n()을 호출해서 n 진법으로 변환된 string을 더해줌
        game += change_n(num)
        num += 1

    p = p - 1    
    # t 길이만큼 while 문을 돌고
    while len(answer) != t:
        # 튜브가 답해야 하는 숫자만 answer에 더해줌
        answer += game[p]   
        p += m
    
    return answer
