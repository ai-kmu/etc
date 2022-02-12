class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        '''
        원소간의 중복이 없는 집합의 성질을 이용
        1. 집합의 크기가 3이 될때까지 집합에 원소를 넣고, 그때의 cnt를 리턴
        2. 우리가 구한 cnt와 기존의 저장된 값 중, 최댓값을 업데이트  
        Accepted 되었지만, 시간복잡도를 좀 더 고려할 필요가 있음
        '''
        # 담을 수 있는 fruits의 개수를 구하는 함수 
        def get_fruits_cnt(idx):
            # 집합 초기화
            st_fruits = set()
            # 개수 초기화
            cnt = 0
            # 입력받은 idx가 fruits의 길이보다 크면 반복문 종료
            while idx < len(fruits):
                st_fruits.add(fruits[idx])
                # 집합에 원소를 추가했을 때, 집합의 길이가 3이 되면 반복문을 강제 종료 
                if len(st_fruits) > 2:
                    break
                cnt += 1
                idx += 1
            return cnt
        
        # 초깃값 설정
        max_fruits_cnt = 0

        for i in range(len(fruits)):
            # 현재 저장된 값과 get_fruits_cnt를 통해 얻은 값 중, 최댓값을 저장
            max_fruits_cnt = max(max_fruits_cnt, get_fruits_cnt(i))
            # max_fruits_cnt에 이미 최댓값이 저장되어 있으면 반복문 강제 종료
            if max_fruits_cnt == len(fruits):
                break
 
        return max_fruits_cnt
