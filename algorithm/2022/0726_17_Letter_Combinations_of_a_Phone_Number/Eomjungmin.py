class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # 번호별 알파벳 딕셔너리 선언
        phone_number = {2: ['a', 'b', 'c'],
                       3: ['d', 'e', 'f'],
                       4: ['g', 'h', 'i'],
                       5: ['j', 'k', 'l'],
                       6: ['m', 'n', 'o'],
                       7: ['p', 'q', 'r', 's'],
                       8: ['t', 'u', 'v'],
                       9: ['w', 'x', 'y', 'z']}
        
        # 입력의 길이가 0인 경우 빈 리스트 출력
        if len(digits) == 0:
            return []
        
        # 정답 리스트 선언
        ans = []
        
        # backtracking 방법을 이용
        def backtracking(cur_str, ind):
            if ind >= len(digits):
                return ans.append(cur_str)
            
            for i in phone_number[int(digits[ind])]:
                cur_str += i
                '''
                현재 cur_str상태에서 다음 인덱스의 digit 값으로 dfs방식과 비슷하게 cur_str에 알파벳 추가
                그리고 digit 길이만큼 다 나왔으면 다시 backtracking하기 위해 뒷 알파벳부터 pop
                '''
                backtracking(cur_str, ind+1) 
                cur_str = cur_str[:-1]
                    
        backtracking("", 0)
        
        return ans
