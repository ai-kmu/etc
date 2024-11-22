# 오답

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0

        total_time = 0
        last_validated_attack_time = 0
        is_poisoned = False
        for elem in timeSeries:
            interval = elem - last_validated_attack_time
            print(f'{elem}: {interval}')
            if is_poisoned is not True:
                last_validated_attack_time = elem
                total_time += duration
                is_poisoned = True
            else:
                interval = elem - last_validated_attack_time
                last_validated_attack_time = elem

                if interval > duration:
                    is_poisoned = False
                    interval = duration
                
                total_time += interval

        return total_time
