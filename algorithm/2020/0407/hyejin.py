# lock의 홀 개수와 key의 돌기 개수 검사
def check_hole(key, lock):
    zero = 0
    # lock의 hole 개수 검사
    for row in lock:
        for i in row:
            if i == 0:
                zero += 1
    # key의 돌기 개수 검사
    for row in key:
        for i in row:
            if i == 1:
                zero -= 1
    
    if zero > 0:
        return False
    return True 

# 2차원 배열을 오른쪽으로 90도 돌리기
def rotate(mat):
    mat_len = len(mat)
    rotate_mat = [[0] * mat_len for _ in range(mat_len)]
    for i in range(mat_len):
        for j in range(mat_len):
            rotate_mat[j][mat_len-1-i] = mat[i][j]
    return rotate_mat

# key와 lock이 맞는지 검사하기
def check_correct(ext_size,lock, key, start_r, start_c, lock_start, lock_end):
    # extend lock 만들기
    ext_lock = [[0] * ext_size for _ in range(ext_size)]
    # key 집어넣기
    for i in range(len(key)):
        for j in range(len(key)):
            # key의 시작점 유의
            ext_lock[start_c+i][start_r+j] += key[i][j]
    
    # lock 집어넣기 => 그때 맞물릴경우 1, 아닐경우는 0 또는 2가 나옴.
    for i in range(lock_start, lock_end):
        for j in range(lock_start, lock_end):
            ext_lock[i][j] += lock[i-lock_start][j-lock_start]
            if ext_lock[i][j] != 1:
                return False
    
    # 빠져나오면 lock부분이 다 1이라는 뜻이므로 완전히 맞물려다는 뜻
    return True
    
    

def solution(key, lock):

    # lock의 홈이 key의 돌기보다 많을 때 transformation을 해도 안됌.
    if check_hole(key, lock) is False:
        return False
    
    # 다 해보기
    # lock 늘리기 => key와 맞물리기 위해서는 길이를 lock_len+(key_len*2)-2로 함
    ext_size = len(lock)+len(key)*2 -2
    # 중간에 lock 배치, lock 시작지점은 key_len-1 index 지점.
    lock_start = len(key) - 1
    lock_end = lock_start + len(lock)
    
    # 90도씩 돌려서 비교. 4번
    for r in range(4):
        # ext_len - key_len +1 = lock_end번을 가로 세로로 체크하면 됌.
        for i in range(lock_end):
            for j in range(lock_end):
                if check_correct(ext_size, lock, key, i, j, lock_start, lock_end) is True:
                    return True
        # 시계방향 90도로 회전
        key = rotate(key)
        
    return False
