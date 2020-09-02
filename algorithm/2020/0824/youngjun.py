#10:30~10:55
#10:55~12:32
class Solution(object):
    def convert(self, s, numRows):

        if numRows==1: # row가 1이면 바로 return
            return s

        answer=['' for i in range(numRows)]
        index=0
        is_blank=False

        for char in s:
            answer[index]+=char

            if index==numRows-1: # 만약 row의 끝에 도착했다면
                is_blank=True
            elif index==0: # 만약 row의 시작이라면
                is_blank=False

            if is_blank==False:
                index += 1  #char을 넣을 자리 이동
            else:
                index -= 1  #char을 넣을 자리 이동

        answer=''.join(answer) # 각 row의 string 합치기
        return answer

if __name__ == '__main__':
    solution=Solution()
    s="ABC"
    print(solution.convert(s,1))


