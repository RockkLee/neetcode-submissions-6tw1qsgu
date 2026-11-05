class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        tups: list[tuple[int,int]] = []
        for i in range(len(position)):
            tups.append((position[i], speed[i]))
        tups.sort()
        
        stack: list[int] = []
        for position, speed in tups:
            stack.append((target - position) / speed)
        
        cnt = 0
        while(len(stack) > 0):
            last = stack[-1]
            cnt += 1
            stack.pop()
            while(len(stack) > 0):
                if stack[-1] <= last:
                    stack.pop()
                    continue
                break
        
        return cnt
