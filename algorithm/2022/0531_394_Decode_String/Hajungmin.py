class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''
        num = 0
        
        # 문자열을 돌며 한 번에 처리
        for i in s:
            # 만약 현재 숫자일 경우 자리 수가 2개 이상일 수 있기 때문에
            # 숫자의 자리수를 구할 수 있도록 num에 10을 곱해주어 현재 숫자에 더함
            if i.isdigit():
                num = num * 10 + int(i)
                
            # 만약 알파벳일 경우 ans에 현재 알파벳을 더해줌
            elif i.isalpha():
                ans += i
               
            # 만약 [가 나왔을 경우 현재까지 문자열과 숫자를 튜플로 묶어서 stack에 저장
            # 이후 ans와 num은 초기화
            elif i == '[':
                stack.append((ans, num))
                ans, num = '', 0
            # 만약 ]이 나왔을 경우 현재까지의 문자열과 숫자를 stack에서 뽑아옴
            # 현재 ans값에 이제까지의 문자열 + 현재 나온 문자열에 * 숫자를 해서
            # ans를 갱신해줌
            else:
                curr_str, curr_num = stack.pop()
                ans = curr_str + curr_num * ans
        # 결론적으로 나온 ans를 반환
        return ans
