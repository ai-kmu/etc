# 1번 선수가 항상 먼저 시작
# 두 선수는 항상 배열의 양 끝에서 선택할 수 있음
# 두 선수가 번갈아가며 선택해서 누적한 값이 큰 player이 승리
# 1번 선수가 승리할 수 있는지 여부를 찾는 문제

class Solution(object):
    def PredictTheWinner(self, nums):
        
        # 빈 딕셔너리 생성
        # key에는 선택된 숫자 튜플, value에는 (player1 점수 총합 - player2 점수 총합)이 저장될 것
        score = {}
        
        # 승자를 비교하기 위한 재귀함수 정의 
        def compare(nums):
            if len(nums) == 1: # 만약 배열 길이가 1이면, 즉 배열에 요소가 하나일 경우
                return sum(nums) # 그때의 요소를 sum해서 return 
            
            else: # 전체 배열 길이가 1보다 클 경우
                key_nums = tuple(nums) # 딕셔너리의 key로 쓰기 위해 불변 타입인 튜플로 만듦
                if key_nums in score: # 딕셔너리에 해당 키가 존재하면
                    return score[key_nums] # 그 때의 value를 return

                else: # 딕셔너리에 없으면 둘 중 더 큰 값을 딕셔러니에 저장하고 리턴
                    # 앞에서부터 재귀탐색, 뒤에서부터 재귀탐색한 값을 비교해서 더 큰 값 찾음
                    score[key_nums] = max(nums[0]-compare(nums[1:]), nums[-1]-compare(nums[:-1]))

                    """
                    print('두 값 비교: ', nums[0]-compare(nums[1:]), nums[-1]-compare(nums[:-1]))
                    print('그때의 배열의 끝값: ', nums[0],nums[-1])
                    print(score)
                    """

                    return score[key_nums] 
                
        # 정답 출력
        if compare(nums) >= 0: # 이긴 경우(비겨도 1번플레이어가 이김)
            return True # True 리턴
        else: # 0보다 작은 경우, 즉 진 경우
            return False # False 리턴
        
        
"""
print문 설명(맨 밑에서부터 보기)

두 값 비교:  226 -226
그때의 배열의 끝값:  233 7 (player2가 7 가져가고 player1이 233 가져가서 승리)
두 값 비교:  -228 228
그때의 배열의 끝값:  5 233 (player2가 5 가져감)
두 값 비교:  -221 -221
그때의 배열의 끝값:  5 7 (player1이 1 가져감)



두 값 비교:  -4 4
그때의 배열의 끝값:  1 5 (player 2가 5를 가져가고 1은 player1이 가져가서 승리)
두 값 비교:  -227 229
그때의 배열의 끝값:  1 233 (player1이 233을 가져갔다)
두 값 비교:  222 -222
그때의 배열의 끝값:  1 7 (player2가 마지막에 7을 가져간다)

INPUT: nums= [1, 5, 233, 7]
"""
