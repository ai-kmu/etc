def solution(progresses, speeds):
    answer = []
    done = [False] * len(progresses)
    
    while sum(answer) != len(progresses):
        the_number_of_done = 0
        i = 0
        while i < len(progresses):
            progresses[i] += speeds[i]
            if progresses[i] >= 100 and not done[i] and (
                i == 0 or (progresses[i-1] >= 100 and done[i-1])
            ):
                the_number_of_done += 1
                done[i] = True
            i += 1
        if the_number_of_done != 0:
            answer.append(the_number_of_done)
    
    return answer
