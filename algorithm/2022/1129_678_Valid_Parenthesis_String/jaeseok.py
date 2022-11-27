class Solution:
    def checkValidString(self, s: str) -> bool:
        # s1 : )을 빼고 다 담을 스택, s2 : *만을 담는 스택
        s1, s2 = [], []
        # s을 순회하면서 우선적으로 (을 제거
        for i in s:
            # )가 아닌 경우 s1에 담음
            if i in ["(", "*"]:
                s1.append(i)
            # )를 만난 경우
            else:
                # s1에 아무것도 없으면 올바른 괄호 완성 불가능
                if not s1:
                    return False
                else:
                    # (부터 처리하기 위해서 *을 따로 s2로 빼냄
                    while s1 and s1[-1] == "*":
                        s2.append(s1.pop())
                    # (이 존재한다면 우선적으로 s1에서 제거, 아니라면 s2에서 * 제거
                    if s1:
                        s1.pop()
                    else:
                        s2.pop()
                # 연산이 끝나면 다시 s1에 담음
                while s2:
                    s1.append(s2.pop())

        # s1에 남은 ( 처리
        # 이제 *은 "" 또는 )로만 동작함
        while s1:
            # s1에서 우선적으로 *를 s2로 빼냄
            while s1 and s1[-1] == "*":
                s2.append(s1.pop())
            # s1이 존재하지 않으면 *만으로 해결 가능
            if not s1:
                return True
            # (이 남아있으면서 ) 역할을 할 s2가 없으면 올바른 괄호 완성 불가능
            if s1 and not s2:
                return False
            # (와 대응하는 *를 가능한 만큼 제거
            while s1 and s2 and s1[-1] == "(":
                s1.pop()
                s2.pop()

        # 모든 과정이 끝났을 때 s1에 남은 것이 없다면 True
        if not s1:
            return True
