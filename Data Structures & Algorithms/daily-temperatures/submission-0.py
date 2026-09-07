class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for j, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                i = stack[-1]
                res[i] = j - i
                stack.pop()
            stack.append(j)
        
        return res

        # Time complexity: O(n)
            # O(n) traversal of temperatures
            # O(n) while loop because stack has at most one of each elem of temperatures
        # Space complexity: O(n)
            # O(n) stack has at most all elems of temperatures
            # O(n) res list, one entry for each elem of temperatures
            