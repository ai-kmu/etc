from collections import Counter

class Solution:
    def count_digits(self, num):
        return Counter(str(num))
    
    def is_matched(self, power_of_two_list, target_number):
        return any(target_number == value for value in power_of_two_list)

    def reordered_power_of_two(self, n):
        power_of_two_list = [self.count_digits(1)]
        target_val = 1
        for _ in range(30):
            target_val <<= 1
            power_of_two_list.append(self.count_digits(target_val))

        target_number = self.count_digits(n)
        return self.is_matched(power_of_two_list, target_number)
