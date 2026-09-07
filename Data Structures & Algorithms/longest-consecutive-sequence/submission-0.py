class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        h = {}
        seen = set()
        max_length = 0
        for n in nums:
            if n in h or n in seen:
                continue

            up = n + 1
            bound_up, length_up = h.get(up, (n, 0))

            down = n - 1
            bound_down, length_down = h.get(down, (n, 0))

            length = 0
            index_up = None
            index_down = None

            if n < bound_up and n > bound_down:
                length = length_up + length_down + 1
                index_up = bound_up
                index_down = bound_down
                h[bound_up] = (bound_down, length)
                h[bound_down] = (bound_up, length)
            elif n < bound_up:
                length = length_up + 1
                index_up = bound_up
                index_down = n
                h[n] = (bound_up, length)
                h[bound_up] = (n, length)
            elif n > bound_down:
                length = length_down + 1
                index_up = n
                index_down = bound_down
                h[n] = (bound_down, length)
                h[bound_down] = (n, length)
            else:
                length = 1
                index_up = n
                index_down = n
                h[n] = (n, 1)
            
            seen.add(n)
            
            if length > max_length:
                max_length = length
        
        return max_length

        # O(n) time
            # Do O(1) work (only hash map, set, and other constant-time operations) for each of n nums
        # O(n) space
            # O(n) space for each hash map and hash set 

                
