# 15. 프로그래머스 - 자물쇠와 열쇠
import numpy as np

# 90도 회전 ... numpy
def rotation(arr, angle):
    rotate_key = np.rot90(arr, 3-angle)
    return rotate_key

# 자물쇠 열리는지 확인
def check(startX, startY, key, lock, p_size, start, end):
    pad = [[0] * p_size for _ in range(p_size)]

    # 패딩 초기화
    for i in range(len(key)):
        for j in range(len(key)):
            pad[startX+i][startY+j] += key[i][j]

    for i in range(start, end):
        for j in range(start, end):
            pad[i][j] += lock[i - start][j - start]
            if pad[i][j] != 1:
                return False

    return True


def solution(key, lock):
    answer = False

    # lock의 시작점과 끝나는 지점
    start = len(key) - 1
    end = start + len(lock)

    # padding이 추가된 배열의 행, 열의 크기
    pad_size = len(lock) + start * 2

    # 4가지만 비교 0, 90, 180, 270
    for a in range(4):
        for i in range(end):
            for j in range(end):
                if check(i, j, key, lock, pad_size, start, end):
                    answer = True
        # key = rotate(key)
        key = rotation(key, a)
    return answer

key_1 = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock_1 = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key_1, lock_1))

# 90도 회전
# def rotate(arr):
# #     length = len(arr)
# #     rotate_key = [[0] * length for _ in range(length)]
# #
# #     for i in range(length):
# #         for j in range(length):
# #             rotate_key[j][length-1-i] = arr[i][j]
# #     return rotate_key

# lock에 2 zero-padding
# def pad_with(vector, pad_width, iaxis, kwargs):
#     pad_value = kwargs.get('padder', 0)
#     vector[:pad_width[0]] = pad_value
#     vector[-pad_width[1]:] = pad_value