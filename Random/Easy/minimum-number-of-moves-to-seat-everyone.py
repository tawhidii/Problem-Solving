class Solution:
    def minMovesToSeat(self, seats, students):
        res = 0
        seats.sort()
        students.sort()
        for i in range(len(students)):
            res += abs(students[i] - seats[i])
        return res
