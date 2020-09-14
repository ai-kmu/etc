class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not s or not p or len(s) < len(p):             # p 또는 s가 빈칸이거나 s보다 p의 길이가 긴 경우에 빈 리스트 반환
            return []
            
        match = {}
        for i in p:                                       # p를 dict에 저장
            if i in match:
                match[i] += 1
            else:
                match[i] = 1
                
        for_match = {}                                    # s를 p의 길이만큼 dict와 deque에 저장
        for_match_deque = deque()
        for i in range(len(p)):
            if s[i] in for_match:
                for_match[s[i]] += 1
            else:
                for_match[s[i]] = 1
            for_match_deque.append(s[i])
            
        s = s[len(p):]                                    # s의 p길이만큼의 앞부분을 제거
        
        answer = []
        answer_id = 0
        if match == for_match:                            # p와 현재 s에 대한 dict가 같은 경우 answer에 index 추가
            answer.append(answer_id)
            
        while s:
            pop_from_match = for_match_deque.popleft()    # deque에서 맨 앞에 원소를 뽑아
            if for_match[pop_from_match] == 1:            # dict에서 제거 ( dict의 value 값이 1인 경우, 아예 제거 )
                del for_match[pop_from_match]  
            else:
                for_match[pop_from_match] -= 1
            for_match_deque.append(s[0])                  # deque에 s의 첫 번째 원소 추가
            
            if s[0] in for_match:                         # dict에 s의 첫 번째 원소 추가
                for_match[s[0]] += 1
            else:
                for_match[s[0]] = 1
                
            s = s[1:]                                     # s의 첫 번째 원소 제거
            
            answer_id += 1                                # index 번호 1 증가
            if match == for_match:                        # 두 개의 dict가 같다면 index를 answer에 
                answer.append(answer_id)
        return answer
