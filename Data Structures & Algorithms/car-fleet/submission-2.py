class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Time: O(nlogn)
        # Space: O(n)

        # (4, 1), (2, 3), (0, 2)
        # Sorted order:
        # stack: (0, 2), (2, 3), (4, 1)
        #
        # Pop last one A, calculate time to reach target
        # Pop next one B, if B reaches A before target, same fleet
        # otherwise, fleet += 1
        #
        # minTime = min(timeA, timeB)
        # Pop next C, if C reaches minTime before target, same fleet
        cars = []
        for pos, speed in zip(position, speed):
            cars.append((pos, speed))

        # Sorting cars by position
        cars.sort(key = lambda car: car[0])

        maxTime = 0
        fleet = 0
        while cars:
            (carPos, carSpeed) = cars.pop()
            timeTaken = (target - carPos) / carSpeed

            if timeTaken > maxTime:
                fleet += 1
                maxTime = timeTaken

        return fleet
            




        
         
        

        

        