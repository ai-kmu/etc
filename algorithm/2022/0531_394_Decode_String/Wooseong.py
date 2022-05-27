class Solution:
    def decodeString(self, s):
        stack = []
        for c in s:
            # ]가 나올 때까지 다 넣어 둠
            if c != ']':
                stack.append(c)

            # ]가 나오면 [] 안을 그 앞에 만큼 반복
            # 뒤에서부터 확인하기 위해 stack 사용
            else:
                # [가 나올 때까지 string 갱신: 뒤로 넣어야 됨
                string = ''
                while stack[-1] != '[':
                    string = stack.pop() + string
                stack.pop()     # [ 제거

                # 이제 숫자 찾기: 역시 뒤로 넣어야 됨
                num = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                num = int(num)

                # string을 num 만큼 반복해서 stack에 넣어 두기
                stack.append(string * num)

        # 다 끝나면 stack -> string
        return ''.join(stack)

'''
ps. 첫 번째 while에는 stack이 없고 두 번째에는 있는 이유는
    일단 둘 다 넣었었는데 첫 번째는 빼도 돌아가고 두 번째는 안 돌아가기 때문입니다
    왜 그런진 정확히 모르겠어요
'''
