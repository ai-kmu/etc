from collections import Counter

class Solution:
    def originalDigits(self, s: str) -> str:
        counter = Counter(s)
        
        answer = []
        
        # 숫자를 영어로 표현한 것 중에서 'z'는 'zero' 밖에 없다. 
        # -> 'z'의 개수를 세는건 'zero'의 개수를 세는 것
        # zero를 전부 다 제거한 후에 'x'의 개수를 세면 'six'의 개수를 세는것과 동일
        # 아래와 같이 number와 해당 number를 세는것과 동일한 id를 정의해 순서대로 제거
        number_to_id = [
            ("zero", "z", 0),
            ("six", "x", 6),
            ("eight", "g", 8),
            ("two", "w", 2),
            ("three", "t", 3),
            ("four", "u", 4),
            ("five", "f", 5),
            ("seven", "v", 7),
            ("nine", "i", 9),
            ("one", "o", 1)
        ]
        
        for remove_str, id, number in number_to_id:
            remove_num = counter[id]
            for _ in range(remove_num):
                answer.append(number)
            
            remove_counter = Counter(remove_str)
            
            for char, count in remove_counter.items():
                counter[char] -= remove_num * count
        
        return ''.join([str(x) for x in sorted(answer)])
