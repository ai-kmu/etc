"""
    다익스트라 비슷하게 맨 아래부터 시작하여 꼭대기로 올라가는 문제로 생각하면 된다.
    단 이 때 최단거리가 아닌 최장거리를 구하면 된다.
    맨 아래부터 시작하여 1, 2, 3, ... , n-1, n으로 올라간다고 하였을 때
    맨아래 부터 중간의 k층까지의 거리를 구하고 이를 반복하여 맨 위층까지 진행시키면 된다..
"""

def solution(triangle):
    for i in range(len(triangle)-2, -1,-1): # triangle의 밑에서 부터 시작
        triangle[i] = [triangle[i][j] + max(triangle[i+1][j], triangle[i+1][j+1]) for j in range(len(triangle[i]))] #현재 층까지의 최대 거리를 구함
    return triangle[0][0] #꼭대기 층을 반환
