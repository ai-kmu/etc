def solution(number, k):
    '''
    세 자리수 수만큼 잘라서 그 중 최대값이 아니면 없애는 방식
    k가 1일 경우에만 최소값 찾음 
    
    하지만 실패..
    '''
    answer = ''
    i = 2
    
    while k:
        # 세자리 자르기
        temp = number[i-2:i+1]
        
        # k가 1일경우 min을 그게 아닐경우에는 max를 찾는다 
        # 찾은 부분을 0으로 처리한다
        if k == 1:
            idx = temp.index(min(temp))
            number = number[0:i-(2-idx)]+ "0" +number[i-(1-idx):]
            break
        if temp[0] != max(temp):
            number = number[0:i-2]+ "0" +number[i-1:]
            k-=1
        
        i+=1
        
    # 전체에서 0인 부분을 없애고 답 리턴
    answer = ''.join(x for x in number if x != '0')
    return answer
