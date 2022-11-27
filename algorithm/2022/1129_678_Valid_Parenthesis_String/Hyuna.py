# 실패 
class Solution:
    def checkValidString(self, s: str) -> bool:
        
        s_list = []
        star_cnt = 0

        # s 에서 하나씩 조회
        for ch in s:
            # ( 일 경우 스택에 쌓아준다
            if ch == '(':
                s_list.append(ch)
            # ) 일 경우 
            elif ch == ')':
                # 스택이 비어있지 않으면 스택을 팝해줌
                if s_list:
                    s_list.pop()
                # 스택이 비어있을 때
                elif not s_list:
                    # *가 0이상이라면 별 개수를 줄여줌
                    if star_cnt > 0:
                        star_cnt -= 1
                    # 별 개수도 0일때 할 수 있는게 없으므로 False 리턴
                    elif not star_cnt:
                        return False
                elif not s_list and star_cnt == 0:
                    return False
            # *일 경우 별 개수 증가
            elif ch == '*':
                star_cnt += 1

        # 스택이 비워지지 않았다면 False, 비워졌다면 True 반환
        if s_list:
            return False
        else:
            return True
        
