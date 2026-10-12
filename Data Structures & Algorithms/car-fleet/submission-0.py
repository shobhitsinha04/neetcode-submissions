class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # we are using a stack in this and each element of the stack would be the fleets 
        # cars recahing at the same tine woudl count as one element of the stack 
        paired = [(p,s) for p,s in zip(position, speed)]
        paired.sort(reverse=True)
        stack = []
        for p, s in paired:
            # the time it takes is being appended using s = d/t
            stack.append((target - p)/s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)