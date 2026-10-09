class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Must sort by position since cars cannot pass
        cars = sorted([[pos, spd] for pos, spd in zip(position, speed)])
        stack = []
       
        for pos, spd in cars:
            time = (target - pos) / spd

            # If car is ahead but slower, collapse stack (fleet)
            while stack and time >= stack[-1]:
                stack.pop()

            stack.append(time)
        
        return len(stack)

        # Time: O(n log(n))
        # Space: O(n)