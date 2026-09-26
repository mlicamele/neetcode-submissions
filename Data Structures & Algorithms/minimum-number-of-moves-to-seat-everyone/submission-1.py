class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count_seats = [0] * (max(seats) + 1)
        count_students = [0] * (max(students) + 1)

        def count_sort(arr, count):
            for num in arr:
                count[num] += 1

        count_sort(seats, count_seats)
        count_sort(students, count_students)

        remain = len(seats)
        i = j = res = 0
        while remain:
            if count_seats[i] == 0:
                i += 1
            if count_students[j] == 0:
                j += 1
            if count_seats[i] and count_students[j]:
                tmp = min(count_seats[i], count_students[j])
                res += abs(i - j) * tmp
                count_seats[i] -= tmp
                count_students[j] -= tmp
                remain -= tmp
        return res