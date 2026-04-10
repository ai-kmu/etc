class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        watering_idx = 0
        water_left = capacity
        is_done = False
        current_steps = 0
        is_backed = False

        while not is_done:
            if watering_idx == len(plants):
                print(current_steps)
                break

            water_steps = water_left - plants[watering_idx]
            if water_steps >= 0:
                water_left = water_steps
                plants[watering_idx] = 0
                watering_idx = watering_idx + 1
                if not is_backed:
                    current_steps += 1
                else:
                    is_backed = False
            else:
                print(f'돌아감. {watering_idx}')
                # 강가로 돌아가기
                current_steps += watering_idx*2 + 1
                water_left = capacity
                is_backed = True

        return current_steps
