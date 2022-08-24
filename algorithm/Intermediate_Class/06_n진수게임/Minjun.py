def solution(n, t, m, p):
    answer = ''
    nums = ''
    
    # 10 -> N진수 변환기
    def tenToN(number, n):
        # 몫, 나머지
        quotient, remainder = divmod(number, n)
        
        # 나머지가 10~16이면 A~F로 변환
        if remainder > 9:
            remainder = convert(remainder)
        
        # 나눌 수 없으면 그대로 나머지로 반환
        if number < n :
            return str(remainder)
        
        # 이전에 받아온 나머지와 현재 계산한 나머지 반환
        return tenToN(quotient, n) + str(remainder)
    
    # 10~16 A~F 맵핑함수
    def convert(num):
        return ['A', 'B', 'C', 'D', 'E', 'F'][num-10]        
    
    
    # t*m만큼 N진수 변환 
    for i in range(t * m):
        nums += tenToN(i, n)
    
    # 튜브가 말해야할 t개만큼 뽑아낸다.
    for i in range(len(nums)):
        if len(answer) < t:
            answer += nums[p-1+i*m]
        else:
            break
            
    return answer
        
