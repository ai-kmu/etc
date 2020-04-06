def rotate(arr):
    # 90도 회전
    return list(zip(*arr[::-1]))

def check(x, y, key, lock, pad_size, start, end):
    pad = [[0] * pad_size for _ in range(pad_size)]

    # 패딩 초기화
    for i in range(len(key)):
        for j in range(len(key)):
            pad[x + i][y + j] += key[i][j]

    # 열쇠가 맞는지 안 맞는지.
    for i in range(start, end):
        for j in range(start, end):
            pad[i][j] += lock[i - start][j - start]
            if pad[i][j] != 1:
                return False

    return True

def solution(key, lock):
    # lock 의 시작 지점
    start = len(key) - 1
    # lock 이 끝나는 지점
    end = start + len(lock)

    # pad가 추가된 배열의 크기
    pad_size = len(lock) + start * 2

    # 회전은 0, 90, 180, 270.
    for i in range(4):
        for j in range(end):
            for k in range(end):
                if check(j, k, key, lock, pad_size, start, end):
                    return True
        key = rotate(key)

    return False


print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
