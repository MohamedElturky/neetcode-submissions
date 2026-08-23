class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = [((target - cars[0][0])/cars[0][1], cars[0][0])]
        count = 1

        for i in range(1, len(position)):
            time = (target - cars[i][0])/cars[i][1]
            if time > stack[-1][0]:
                stack.append((time,cars[i][0]))
                count +=1

        return count
        