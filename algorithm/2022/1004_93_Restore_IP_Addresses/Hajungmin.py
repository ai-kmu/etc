class Solution(object):
    def restoreIpAddresses(self, s):
        ans = []
        
        # 백트래킹 함수
        # 처음 시작 노드의 숫자 개수를 1, 2, 3개로 바꿔가며 탐색
        # digits_num은 현재까지 만들어진 ip를 저장해놓는 리스트
        def backtrack(digits_num, index,s):
            # 만약 만들어진 ip의 길이가 4이상이면 return
            if len(digits_num) > 4:
                return
            
            # 만약 현재 가리키는 인덱스가 주어진 수의 길이보다 크고
            # 만들어진 ip가 4라면 현재 만들어진 수를 string으로 만들어서 정답에 추가
            if index >= len(s):
                if len(digits_num) == 4:
                    ans.append(".".join(digits_num))
                    return
                
                else: return
            
            # 만약 현재 숫자가 0이면 0을 추가하고 다음 단계로 탐색
            # 0이 숫자의 앞자리가 되는 경우를 방지 ex. 1.0.1.023
            if s[index] == '0':
                return backtrack(digits_num + ['0'], index + 1, s)
            
            # 일반적인 경우 현재 만들어진 ip에 해당 값을 추가한 후에 백트래킹 실행
            backtrack(digits_num + [s[index]], index + 1, s)

            # 숫자를 두 개씩 묶기 위해 만약 현재 인덱스가 주어진 수의 길이에서 2를 뺀 것보다 작으면
            # 숫자 2개 한번에 추가해주고 인덱스 2 늘려서 백트래킹
            if index <= len(s) - 2:
                backtrack(digits_num + [s[index:index + 2]], index + 2, s)
            
            # 숫자를 세 개 추가하는 부분인데 이 부분은 만들어진 숫자가 255를 넘는지 추가로 확인
            if index <= len(s) - 3 and int(s[index:index + 3]) <= 255:
                backtrack(digits_num + [s[index:index + 3]], index + 3, s)
        
        backtrack([], 0, s)
        return ans 
