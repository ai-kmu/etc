# flag라는 변수로 내가 지금 숫자 몇을 얼마만큼 더해야 하는지를 알아냄
# 그 후 answer는 내가 2개를 한꺼번에 추가해 n이상을 구한 경우를 제외하면 계속 1이 더해지는 만큼 더해줌
class Solution:
    def magicalString(self, n):
        if n ==0:
            return 0
        arr = [1,2,2]
        answer, flag = 1 ,2
        while len(arr) < n:
            arr += [3-arr[-1]] * arr[flag]
            if len(arr) <= n:
                answer += (arr[-1] == 1) * arr[flag]
            else:
                answer += (arr[-1] == 1)
            flag+=1

        return answer
