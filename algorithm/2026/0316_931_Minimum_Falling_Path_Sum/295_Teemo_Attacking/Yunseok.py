class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        last_atk = timeSeries[0]
        num_of_seconds = duration
        for attack_time in timeSeries[1:]:
            if attack_time - last_atk >= duration:
                num_of_seconds += duration
            elif attack_time - last_atk < duration:
                num_of_seconds += attack_time - last_atk

            last_atk = attack_time

        return num_of_seconds
