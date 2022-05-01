'''
[로직 설명]
ex. n = 4, k = 3, 일때 정답 : "1324"
n = 4일때 시작 : 남은값{1, 2, 3, 4}

#1. 올림값과 나머지값을 계산한다.
k / (n - 1)! 의 올림값 = ceil(3 /(4 - 1)!) = 1
남은값{1, 2, 3, 4} 중 1번째 수, 정답으로 pop -> 정답값{1}, 남은값{2, 3, 4}

(k % (n - 1)!) = 3 % (4 - 1)! = 3 % 6 = 3(갱신된 k 값, #2에 대입)

#2. (n - 1) -> (n - 2)로 갱신, 갱신된 k 값 사용
3 /(n - 2)! 의 올림값 = ceil(3 / (4 - 2)!) = 2
남은값{2, 3, 4} 중 2번째 수, 정답으로 pop -> 정답값{1, 3}, 남은값{2, 4}

(3 % (n - 2)!) = 3 % (4-2)! = 1(갱신된 k 값, #3에 대입)

#3. (n - 2) -> (n - 3)로 갱신, 갱신된 k 값 사용
1 /(n - 3)! 의 올림값 = ceil(1 / (4 - 3)!) = 1
남은값{2, 4} 중 1번째 수, 정답으로 pop -> 정답값{1, 3, 2} 남은값{4}

(1 % (n - 3)!) = 1 % (4 - 3)! = 0

#4.마지막 남은 {4} 값 정답으로 넣어주면 -> 정답값 "1324"
'''
import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        answer = ""
        left_num = list(range(1, n + 1))  # 남은값 {}
        
        while(len(left_num)):  #1. ~ #4. 과정 반복
            n_num = math.ceil(k / math.factorial(n - 1))  # ceil로 n번째 수(n_num) 구하기
            answer += str(left_num.pop(n_num - 1 ))  # n번째 수 pop 후, answer(정답값)에 추가
            k = k % math.factorial(n-1)  # 다음단계에 사용할 K 갱신
            n -= 1  # n 갱신         
            
        return answer   
        
        
