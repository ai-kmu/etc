class Solution:
    def isPalindrome(self, x: int) -> bool:
        # 예외처리 1: 음수는 무조건 안 됨
        if x < 0:
            return False
        # 예외처리 2: 한 자리는 무조건 됨
        elif x < 10:
            return True

        row = str(x)       # string 변환하고
        pal = row[::-1]    # 뒤집어서
        return row == pal  # 같은지 확인
