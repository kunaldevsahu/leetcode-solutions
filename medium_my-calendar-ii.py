from leetcode import evaluate


class MyCalendar:

    def __init__(self):
        self.bookings = []
        
    def book(self, start: int, end: int) -> bool:
        # Check for overlaps with existing bookings
        for a, b in self.bookings:
            if start < b and end > a:
                new_start = max(a, start)
                new_end = min(b, end)

                if self.check(new_start, new_end):
                    return False

        self.bookings.append((start, end))
        return True
    
    def check(self, start: int, end: int) -> bool:
        overlap_count = 0
        
        for a, b in self.bookings:
            if start < b and end > a:
                overlap_count += 1
                if overlap_count == 2:
                    return True

        return False        

class Solution:
    def function(self, x: int) -> int:
        return x


if __name__ == "__main__":
    inputs = [
        (123, ),
    ]
    outputs = [
        (123),
    ]
    x = Solution()
    evaluate(x.function, inputs, outputs)
