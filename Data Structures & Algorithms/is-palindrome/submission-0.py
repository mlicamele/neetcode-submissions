class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([c for c in s if (ord(c) >= ord('A') and ord(c) <= ord('Z')) or (ord(c) >= ord('0') and ord(c) <= ord('9')) or (ord(c) >= ord('a') and ord(c) <= ord('z'))])
        s = s.lower()

        for i in range(len(s)//2 + len(s) % 2):
            if s[i] != s[len(s) - i - 1]:
                return False
        return True

        # O(n) time
            # O(n) character filter step
            # O(n) join step
            # O(n) lower step
            # O(n/2) = O(n) traversal palindrome check
        # O(n) space --> need to improve later to O(1)!!!
            # O(n) new string made
