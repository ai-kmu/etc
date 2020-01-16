############ sol1 ###############
#### time out ####
iteration = int(input())
num_list = []
total_length = 0

for iter in range(iteration):
    tmp_list = list(map(int, input().split()))
    num_list.append(tmp_list)

num_list.sort()
start, end = num_list.pop(0)

for iter in range(iteration - 1):
    tmp_start, tmp_end = num_list[iter]
    
    if start < tmp_start and tmp_end < end:
        continue
    total_length += (end - start)
    
    if tmp_start < end:
        total_length -= (end - tmp_start)
    
    start, end = tmp_start, tmp_end

total_length += (end - start)

print(total_length)

############ sol2 ###############
##### time out #####
# 선 긋기 문제

# 몇 회의 선 긋기를 할 것인지의 횟수를 iteration변수에 담기
iteration = int(input())
num_list = []
total_length = 0

for iter in range(iteration):
    tmp_list = list(map(int, input().split()))
    num_list.append(tmp_list)
    
num_list.sort()
start, end = num_list.pop()

for iter in range(iteration - 1):
    tmp_start, tmp_end = num_list[iter]
    
    if start < tmp_start < end:
      if end < tmp_end:
        end = tmp_end

    # end < tmp_start
    else:
      total_length += (end - start)
      start = tmp_start
      end = tmp_end

total_length += (end - start)

print(total_length)
