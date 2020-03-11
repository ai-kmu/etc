# 11. 기능개발

def solution(progresses, speeds):
    answer = []
    accept_time = 0
    finished_time = []
    for progress, speed in zip(progresses, speeds):
        accept_time += 1
        course_rate = progress + accept_time * speed
        while course_rate < 100:
            accept_time += 1
            course_rate = progress + accept_time * speed
        finished_time.append(accept_time)
        accept_time = 0
    # print('finished_time : ', finished_time)

    front = 0
    for index in range(len(finished_time)):
        if finished_time[front] < finished_time[index]:
            answer.append(index - front)
            front = index
    answer.append(len(finished_time) - front)
    return answer

progress_1 = [93, 30, 55]
speed_1 = [1, 30, 5]
print(solution(progress_1, speed_1))

