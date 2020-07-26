class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # substring을 담을 array 초기화
        answer = []
        
        # s가 empty string일 경우
        if s == "":
            return 0
        
        # sub string의 max number 초기화
        max_num = 0
        
        # 전체 string에 대한 for loop
        for char in s:
            # char이 substring에 없을 경우에 추가가능
            if char not in answer:
                answer.append(char)
            # 만약 들어있을 경우, substring이 되지 못함
            else:
                # 현재 substring과 max_num을 비교
                max_num = max(len(answer), max_num)
                '''
                substring에 char을 추가하고 
                첫번째 char index의 뒤의 element들로 substring을 만듦
                ex) ['a', 'b', 'c', 'a'] => ['b', 'c', 'a']
                '''
                answer.append(char)
                start_i = answer.index(char) + 1
                answer = answer[start_i:]
        
        # 만약 s의 length가 1일 경우에는 max값이 계산되지 않음. 한번 더 실행해주기
        max_num = max(len(answer), max_num)

        return max_num
