def solution(words):    
    
    words.sort()
    
    # make zero vector
    counter_vector = []
    for i in range(len(words)):
        counter_vector.append([0 for j in range(len(words[i])+1)])
    
    # fill counter_vector
    word_stack = ['0']*MAX_COUNT
    for i in range(len(words)):
        fill_current_vector(i,words,counter_vector,word_stack)
    
    #print(counter_vector)

    # return answer
    answer = 0
    for i in range(len(words)):
        answer += sum(counter_vector[i])
    return answer




MAX_COUNT = 1000


def fill_current_vector(current_word,words,counter_vector,word_stack):
    while(1):
        current_step = counter_vector[current_word].index(0)
        word_stack[current_step] = words[current_word][current_step]
        
        for i in range(current_word,len(words)):
            if current_step > len(words[i])-1 : break
            if word_stack[current_step] == words[i][current_step] and counter_vector[i].index(0) == current_step :
                counter_vector[i][current_step] = 1
            else : break
        
        # break condition 1
        if counter_vector[current_word][-2] == 1 : break
        # break condition 2, 3
        if current_word == len(words)-1 : break
        else:
            if counter_vector[current_word+1][current_step] == 1 : pass
            else : break

