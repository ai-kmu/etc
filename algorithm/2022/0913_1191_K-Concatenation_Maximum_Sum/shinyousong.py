class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        # 저장: 전체합
        store_sum = sum(arr)
        
        # case 0: 0이 답
        res0 = 0
        # case 1: 전체합이 답
        res1 = store_sum * k
        # case 2: 좌우합(+전체합*k)이 답
        # case 3: 줃간합이 답
           
        # 부분합들을 merge, 안해도 될듯?
        # 뒤집어서 뒤에서부터
        arr.reverse()
        # 리스트 1개에 대한 merge, 변화가 없을때까지
        flag = 0
        while flag != len(arr):
            # 플래그 초기화
            flag = len(arr)
            # 방향 초기화
            sign = 1 if arr[-1] >= 0 else 0
            # 거꾸로 돌기
            for i in range(len(arr)-1, 0, -1):
                # 부호가 같으면 합침
                if sign == 1 and arr[i-1] >= 0:
                    arr[i-1] += arr[i]
                    del arr[i]
                elif sign == 0 and arr[i-1] < 0:
                    arr[i-1] += arr[i]
                    del arr[i]
                # 부호가 다르면 합치지 않고, 부호를 바꿔줌
                else:
                    sign = (sign+1)%2
            # 다 돌았으면 다리를 이어봄
            for i in range(len(arr)-2, 0, -1):
                # 무조건 이어도 되는 경우만 이음
                if arr[i] < 0 and arr[i+1] + arr[i] >= 0  and arr[i-1] + arr[i] >= 0:
                    arr[i-1] = arr[i-1] + arr[i] + arr[i+1]
                    del arr[i+1]
                    del arr[i]
                    i = i-1
        # 1번이 끝인 경우를 반환
        if k == 1:
            return max(arr) if max(arr) > 0 else 0
        
        # 좌우합 구하기
        plusleft = 0
        plusleftmax = 0
        plusright = 0
        plusrightmax = 0
        for i in range(len(arr)):
            plusright += arr[i]
            if plusright >= plusrightmax:
                plusrightmax = plusright
        for i in range(len(arr)-1, -1, -1):
            plusleft += arr[i]
            if plusleft >= plusleftmax:
                plusleftmax = plusleft
        res2 = plusleftmax+plusrightmax
        res2 = res2 if store_sum < 0 else res2 + store_sum*(k - 2)
        
        # 중간합 구하기
        idx = len(arr)/2
        # 중간을 기점으로 이어지는 경우
        plusleft = 0
        plusleftmax = 0
        plusright = 0
        plusrightmax = 0
        # 단일값이 제일 큰 경우
        solo = 0
        # 중간을 기점으로 이어지지 않는 경우
        left = 0
        leftmax = 0
        right = 0
        rightmax = 0
        for i in range(len(arr)):
            plusright += arr[i]
            if plusright >= plusrightmax:
                plusrightmax = plusright
            if arr[i] > solo:
                solo = arr[i]
            left += arr[i]
            if left < 0:
                left = 0
            if left > leftmax:
                leftmax = left
        for i in range(len(arr)-1, -1, -1):
            plusleft += arr[i]
            if plusleft >= plusleftmax:
                plusleftmax = plusleft
            if arr[i] > solo:
                solo = arr[i]
            right += arr[i]
            if right < 0:
                right = 0
            if right > rightmax:
                rightmax = right
        res3 = max(solo, plusrightmax+plusleftmax, leftmax, rightmax)
        # 결과
        res = [res0, res1, res2, res3]
        print(res)
        m = (10**9+7)
        return max(res)%m
