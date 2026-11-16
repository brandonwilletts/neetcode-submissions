class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        flights = {src: [] for src, dst in tickets}
        tickets.sort(reverse = True)

        for src, dst in tickets:
            flights[src].append(dst)

        output = []
        stack = ["JFK"]

        while stack:
            if stack[-1] in flights and flights[stack[-1]]:
                stack.append(flights[stack[-1]].pop())
            else:
                output.append(stack.pop())

        return output[::-1]