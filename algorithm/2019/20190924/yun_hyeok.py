def is_palindrome(s):
    for i in range(0, len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def solution(s):
    for i in range(len(s), 0, -1):
        for j in range(len(s) - i + 1):
            if is_palindrome(s[j:j + i]):
                return i


if __name__ == '__main__':
    test_set = [("abcdcba", 7),
                ("abacde", 3)
                ]
    for i, o in test_set:
        assert solution(i) == o
