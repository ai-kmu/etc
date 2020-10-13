class Solution:
    # parent로 올라가면서 answer 찾음.
    def make_answer(self, canon_path, curr_idx):
        if curr_idx == 0:
            return '/'
        curr = canon_path[curr_idx][1]
        answer = curr
        while curr_idx >= 0:
            curr_idx = canon_path[curr_idx][0]
            if curr_idx == 0:
                answer = '/' + answer
                break
            answer = canon_path[curr_idx][1] + '/' + answer
        return answer
    
    
    def simplifyPath(self, path: str) -> str:
        # path에서 추출한 폴더들을 (parent index, base name)으로 저장하기
        canon_path = [(0,'/')]
        # 현재 parent index
        parent_idx = 0
        # /를 제외한 string
        base = ''
        # 현재 index
        i = 1
        while i <= len(path):
            # i가 '/'를 가리키거나 마지막까지 갔을 때
            if i == len(path) or path[i] == '/':
                # base가 ..일 경우는 parent_idx를 이전 parent_idx로 올라감.
                if base == '..':
                    parent_idx = canon_path[parent_idx][0]
                # base가 empty string or '.'가 아닐 때, 폴더 만들기
                elif base != '' and base != '.':
                    canon_path.append((parent_idx, base))
                    parent_idx = len(canon_path) - 1
                base = ''
            else: # '/'를 만나지 않았을 때 base를 추가
                base += path[i]
            i += 1
            
        return self.make_answer(canon_path, parent_idx)
