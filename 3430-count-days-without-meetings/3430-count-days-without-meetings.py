class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort() # Sort meetings by start day
        available_days = 0
        last_meeting_end = 0

        for meeting in meetings:
            start, end = meeting
            # Calculate available days between last meeting and current meeting
            if start > last_meeting_end:
                available_days += start - last_meeting_end - 1
            last_meeting_end = max(last_meeting_end, end)

        # Calculate available days after the last meeting
        if last_meeting_end < days:
            available_days += days - last_meeting_end

        return available_days