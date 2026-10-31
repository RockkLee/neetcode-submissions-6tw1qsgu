class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: list[tuple[int, int]] = []
        results: list[int] = [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            if len(stack) == 0:
                stack.append((i, t))
                continue
            last_i, last_t = stack[-1]
            while len(stack) > 0 and last_t < t:
                _, last_t = stack.pop()
                results[last_i] = i - last_i
                if len(stack) > 0:
                    last_i, last_t = stack[-1]
            stack.append((i, t))
        return results