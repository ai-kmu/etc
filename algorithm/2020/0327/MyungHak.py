"""
1. laser는 () 가 나올때 쇠막대를 절단한다. 따라서 ()를 레이저가 쏴진 것을 뜻하는 문자인 "/"로 바꾼다.
2. laser가 쏴졌을 때 그 밑에 있는 막대의 수만큼 막대가 늘어난다. 
   밑에 있는 막대의 수는 "("가 나온 수에 ")"가 나온 수를 빼면 된다. 
   이렇게 원래 있던 막대수에 더해진 막대를 split_bar라는 변수에 저장해둔다. 
3. 이제 원래 있던 막대수에 split_bar의 수를 더하면 정답이 나온다.
   이때 원래 있던 막새수는 전체 문자열에서 레이저를 쏜것을 의미하는 문자를 제거하고 2로 나누면 구할수 있다.
"""

def solution(arrangement):
    arrangement = arrangement.replace("()", "/")  # 레이저가 발사된것을 굳이 2문자로 표현하면 조건문으로 검사하기 귀찮아지므로 바꾸어줌
    split_bar = 0
    answer = 0
    for word in arrangement:
        if word == '(':             #밑에 있는 막대의 수를 증가시킴
            split_bar += 1
        elif word == ")":           #밑에 있는 막대의 수를 감소시킴
            split_bar -= 1
        else:                       #레이저가 발사된 경우
            answer+=split_bar
    arrangement = arrangement.replace("/", "")
    
    return answer + int(len(arrangement)/2)
