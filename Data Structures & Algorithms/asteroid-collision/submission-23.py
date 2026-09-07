class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        if len(asteroids) <= 1:
            return asteroids
        if len(asteroids) == 2:
            a = asteroids[0]
            a2 = asteroids[1]
            if (a < 0 and a2 > 0):
                if abs(a) > abs(a2):
                    return [a]
                elif abs(a) < abs(a2):
                    return [a2]
                else:
                    return []
        stack = []
        stack.append(asteroids[0])
        i = 1
        push = False
        while i < len(asteroids):
            a = asteroids[i]
            # print(stack)
            # print(a)
            if not stack:
                stack.append(a)
                i += 1
                continue
            while stack:
                a2 = stack.pop()
                if (a < 0 and a2 > 0):
                    if abs(a) > abs(a2):
                        push = True
                        continue
                    elif abs(a) < abs(a2):
                        push = False
                        stack.append(a2)
                        break
                    else:
                        push = False
                        break
                else:
                    push = False
                    stack.append(a2)
                    stack.append(a)
                    break
            if push and not stack:
                stack.append(a)
            i += 1
        return stack
            