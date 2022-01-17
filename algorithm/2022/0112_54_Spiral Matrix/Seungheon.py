# 발표자 comment
# 사소하지만 left를 필요할 때에만 만들어주는것이 좋을것 같습니다.

class Solution(object):
    def spiralOrder(self, matrix):
    
        # 외곽부터 한칸씩 들어가면서 aswer에 추가하는 방식으로 코드작성
        
        # m = 행 길이
        m = len(matrix)
        # n = 열 길이 
        n = len(matrix[0])
        answer = []
        # 가장 바깥부터 현재 몇번째 박스인지
        i = 0
        #모든 박스를 검사할때까지
        while m>0 and n>0:
            
            # 박스위 맨 윗줄 answer에 추가
            answer += matrix[i][i:i+n]
            # left에 박스의 왼쪽부분을 저장
            left = []
            for j in range(m-2):
                #박스의 오른쪽을 answer에 추가,
                answer.append(matrix[1 + j+i][-1-i])
                #박스의 왼쪽을 저장 
                left.append(matrix[-2-j-i][i])
            #(중앙부분 중복제거를 위해 if문 사용)
            # 박스의 아랫부분 answer에 추가 
            if m != 1 :
                answer += matrix[i+m-1][i:n+i][::-1]
            # 박스의 왼쪽부분 answer에 추가
            if n != 1 :
                answer += left
            #안쪽박스로 위치변경
            m -= 2
            n -= 2
            i += 1
        return answer
