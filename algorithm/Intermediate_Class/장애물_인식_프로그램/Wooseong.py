import sys

def search(row, col):
    if row <= -1 or row >= N or col <= -1 or col >= N:
        return False

    if array[row][col] == '1':
        count.append(1)
        array[row][col] = '0'

        search(row - 1, col)
        search(row + 1, col)
        search(row, col - 1)
        search(row, col + 1)

        return True
    
    return False

N = int(sys.stdin.readline())

count = []
array = []
for _ in range(N):
    array.append([i for i in sys.stdin.readline().rstrip()])

answer = 0
answer_list = []
for row in range(N):
    for col in range(N):
        if search(row, col):
            answer += 1
            answer_list.append(len(count))
            count = []

print(answer)
answer_list.sort()
for i in answer_list:
    print(i)
