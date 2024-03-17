# 풀이실패
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # 첫 인덱스에서부터 시작
        # 첫 인덱스 기준 리스트에서 홀수 개수 만족할때까지 서브어레이 탐색 후 저장
        # 홀수 개수 만족하면, 뒤에 다음 홀수 나올때까지 반복 (홀수 개수 파악하는 변수 필요)
        # 다음 값에서 홀수가 나오거나 탐색 완료하면 다음 인덱스로 이동
        # 서브어레이 개수 리턴
        from collections import deque

        nums = deque(nums)

        sub_arr = []
        temp_arr = []
        check_odd = 0
        sub_ans = 0
        count_odd = 0

        while nums:
            for i in nums:
                if i % 2 != 0:
                    count_odd += 1
                    print(count_odd)
                temp_arr.append(i)
                print('temp: ', temp_arr)
                if i % 2 != 0:
                    check_odd += 1
                if check_odd == k:
                    sub_arr.append(temp_arr)
                if check_odd == (k+1):
                    temp_arr = []
                    check_odd = 0
                    count_odd = 0
                    break
            print('count: ', count_odd)
                
            # print(sub_arr)
            if count_odd <= k:
                temp = []
                count_odd = 0
            nums.popleft()
