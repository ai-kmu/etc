# 풀이실패하고 정답 봤습니다..
# 리뷰 안해주셔도 돼요

class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        res = 0  # 결과값으로 반환할 가능한 부분배열의 개수를 저장하는 변수
        i = j = 0  # 부분배열의 시작과 끝 인덱스를 나타내는 변수
        d = dict()  # 값과 해당 값의 마지막 등장 인덱스를 저장하는 딕셔너리

        while j < len(nums):
            t = {k: v for k, v in d.items()}  # 딕셔너리 생성
            for k, v in t.items():
                if abs(k - nums[j]) > 2:
                    i = v + 1  # 현재 값과의 차이가 2를 초과하는 경우, i를 갱신하여 새로운 부분배열의 시작 인덱스로 설정
                    d.pop(k)  # 딕셔너리에서 해당 값 제거

            d[nums[j]] = j  # 딕셔너리에 현재 값과 해당 값의 인덱스를 추가
            res += j - i + 1  # 가능한 부분배열의 개수를 누적
            j += 1  # 다음 값으로 이동

        return res  # 가능한 부분배열의 개수 반환
