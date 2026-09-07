class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        OPERATORS = ['+', '-', '*', '/']
        for t in tokens:
            if t in OPERATORS:
                b = stack.pop()
                a = stack.pop()
                if t == '+':
                    stack.append(a + b)
                elif t == '-':
                    stack.append(a - b)
                elif t == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(a / b))
            else:
                stack.append(int(t))
        return stack.pop()

        # O(n) time
            # O(n) for loop because O(1) or O(1) amortized for each of n tokens
                # Checking if in OPERATORS O(1) since constant size
        # O(n) space
            # O(n) stack because at most n elems in stack