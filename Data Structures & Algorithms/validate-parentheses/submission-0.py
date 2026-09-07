class Solution:
    def isValid(self, s: str) -> bool:
        OPEN = ['(', '{', '[']
        CLOSE = [')', '}', ']']
        stack = []
        for c in s:
            if c in OPEN:
                stack.append(c)
            else:
                if not stack or OPEN.index(stack.pop()) != CLOSE.index(c):
                    return False
        return not stack

        # O(n) time
            # O(n) for loop because n iters of constant-time O(1) operations (amortized for stack pop)
                # Getting index/checking if c in list is constant because OPEN and CLOSE are constant size
        # O(n) space
            # Stack has at most n elems
        


