'''
b + y = N * M
y = (N-2) * (M-2) = N * M - 2 * (N + M) + 4
therefore
    b = 2 * (N + M) - 4

2N = b - 2M + 4
2 * (b + y) = 2 * N * M = (b - 2M + 4) * M
            = b * M - 2 * M * M + 4 * M
2 * M ** 2 - (b + 4) * M + 2 * (b + y) = 0
therefore
    M = [(b + 4) + sqrt{(b + 4) ** 2 - 16 * (b + y)}] // 4
'''
def solution(b, y):
    M = ((b + 4) - ((b + 4) ** 2 - 16 * (b + y)) ** 0.5) // 4
    N = (b - 2 * M + 4) // 2
    
    if M < N:
        M, N = N, M
    
    return [M, N]
