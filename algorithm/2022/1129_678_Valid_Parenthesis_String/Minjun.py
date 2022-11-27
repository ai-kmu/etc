'''
* 이 (인 경우와 )인 경우를 동시에 고려해서 푼다

*의 개수는 ( 가 ) 보다 적을 때 중요하다,
( + * 의 개수보다 )의 개수가 현재까지의 ( 보다 많다면,  -> *이 (의 개수를 채워주지 못한다면 실패

'''

class Solution:
    def checkValidString(self, s: str) -> bool:
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            else:
                left -= 1
            if c == ')':
                right += 1
            else:
                right -= 1
            if right > 0:
                break
            if left < 0:
                left = 0
            
        if left == 0:
            return True
        return False
