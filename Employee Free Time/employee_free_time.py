# 759. Employee Free Time
# https://leetcode.com/problems/employee-free-time/description/


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """

        sorted_schedule = list()
        for emp_list in schedule:
            for s in emp_list:
                sorted_schedule.append(s)

        sorted_schedule = sorted(sorted_schedule, key=lambda x: (x.start, -x.end))
        result = list()
        end_time = sorted_schedule[0].end
        for idx in range(1, len(sorted_schedule)):
            if end_time >= sorted_schedule[idx].end:
                continue
            if end_time < sorted_schedule[idx].start:
                result.append(Interval(end_time, sorted_schedule[idx].start))
            end_time = sorted_schedule[idx].end

        return result
