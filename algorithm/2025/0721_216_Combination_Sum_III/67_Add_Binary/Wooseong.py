class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = "0b" + a  # 2진법 flag 추가
        b = "0b" + b  # 2진법 flag 추가
        return str(bin(int(a, 2) + int(b, 2)))[2:]  # 덧셈 > 2진법변환 > 2진법 flag 제거
