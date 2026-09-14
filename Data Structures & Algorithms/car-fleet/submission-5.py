class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [(target - p) / s for p, s in zip(position, speed)]
        cars = [(p, s, t) for p, s, t in zip(position, speed, time)]
        cars.sort(reverse=True)
        count = 0
        old_t = None
        for car in cars:
            p, s, t = car
            if old_t is not None and t <= old_t:
                continue
            else:
                count += 1
                old_t = t
        return count
            
