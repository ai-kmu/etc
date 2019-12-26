def solution(begin, target, words):
    count = 0
    answer = [begin]
    
    while True:
        for word in answer:
            temp=[]
            if word == target:
                return count

            for i in range(len(words)-1, -1, -1):  
                print("i: ", i)
                next_word = words[i]
                if sum([x!=y for x, y in zip(word, next_word)]) == 1:
                    temp.append(words.pop(i))
                    
        if not temp:
            return 0
        
        answer = temp
        count += 1
