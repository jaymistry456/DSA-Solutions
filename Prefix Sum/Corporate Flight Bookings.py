# https://leetcode.com/problems/corporate-flight-bookings/description/

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        # brute-force
        # TC: O(n^2), SC: O(1)
        res = [0] * (n + 1)
        for i in range(len(bookings)):
            for j in range(bookings[i][0], bookings[i][1] + 1):
                res[j] += bookings[i][2]
        return res[1:]


        # optimal
        # TC: O(n), SC: O(n)
        arr = [0] * (n + 2)
        for i in range(len(bookings)):
            arr[bookings[i][0]] += bookings[i][2]
            arr[bookings[i][1] + 1] -= bookings[i][2]
        res = [0] * (n + 2)
        curr = 0
        for i in range(len(arr)):
            curr += arr[i]
            res[i] = curr
        return res[1:n+1]