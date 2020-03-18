def solution(priorities, location):
    count = 1
    waits = {}
    for i in range(len(priorities)):
        waits[i] = priorities[i]

    values = list(waits.values())
    max_value = max(values)
    number_of_max = values.count(max_value)

    while(1):
        temp = next(iter(waits.items()))
        key_first, value_first =  temp[0], temp[1]
        if value_first == max_value:
            if key_first == location:
                answer = count
                break
            else:
                del waits[key_first]
                count += 1
                number_of_max -= 1
                if number_of_max == 0 :
                    while(1):
                        max_value -= 1
                        number_of_max = values.count(max_value)
                        if number_of_max > 0 : break

        else : 
            del waits[key_first]
            waits[key_first] = value_first
        answer = 0
    return answer
