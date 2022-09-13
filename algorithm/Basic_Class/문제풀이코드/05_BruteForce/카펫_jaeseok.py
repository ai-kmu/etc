def solution(brown, yellow):
    # brown이 8, yellow가 1이 최소조건인 경우는 width와 height가 모두 3인 경우
    width = 3
    height = 3
    # width에 의해 height가 결정되므로 width를 1씩 더해가면서 yellow와 brown의 개수가 조건과 같을 때까지 계속 width에 1을 더함
    # width는 항상 height보다 같거나 커야 함
    while True:
        if (width - 2) * (height - 2) == yellow and width >= height:
            return [width,height]
        width += 1
        height = (brown - 2 * width) / 2 + 2
