class Solution:
    def minFlips(self, target: str) -> int:
		answer = 0 
		ex = '0'                    # ex-character
		for char in target:         # compare all characters 
            if char!=ex:            #  if char differ with ex-character, we have to flip bulbs once.
                answer += 1
                ex = char
        return answer
