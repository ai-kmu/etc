class Solution(object):
    # 해당 요소를 체크 했을 때 -1로 저장하여 기록하고 해당 요소를 배열의 인덱스로 입력하여 그 결과값이 최초로 -1이 나오면
    # 해당 요소는 이미 체크했다는 의미이므로 이 상태에서 인덱스 i에서 시작할 때 반복을 기록한 횟수를 이용하여 최대 길이 구한다.
    def arrayNesting(self, List):
        #:type nums: List[int]
        #:rtype: int
        for i in range(len(List)):
            cnt = 0
            value = List[i] # 처음 시작값을 저장
            while value != -1: 
              cnt += 1
              List[i] = -1 # 체크한 요소를 -1로 저장
              value = List[value] # 처음 시작값을 배열의 인덱스로 다시 대입하여 배열의 요소값 출력
            max_length = max(cnt, max_length) # 인덱스 i에서 시작했을 때의 반복 횟수와 전의 최대 길이 중 최댓값을 출력
        return max_length

