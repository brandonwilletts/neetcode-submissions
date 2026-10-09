class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[pos, spd] for pos, spd in zip(position, speed)]
        stack = [] # Times

        # Must sort by position since cars cannot pass
        for pos, spd in sorted(cars):
            time = (target - pos) / spd

            # If car is ahead but slower, collapse stack (fleet)
            while stack and time >= stack[-1]:
                stack.pop()

            stack.append(time)
        
        return len(stack)

        # Time: O(n log(n))
        # Space: O(n)