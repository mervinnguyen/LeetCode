#You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

#Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge them if necessary).

#Return intervals after the insertion.

#Example 1:
#Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
#Output: [[1,5],[6,9]]

#Example 2:
#Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
#Output: [[1,2],[3,10],[12,16]]
#Explanation: Because the newInterval [4,8] overlaps with [3,5],[6,7],[8,10].

class Solution(object):
    def insert(self, intervals, newInterval):
        merge = []
        for i in range(len(intervals)):
            if intervals[i][1] < newInterval[0]:
                merge.append(intervals[i])
            elif intervals[i][0] > newInterval[1]:
                merge.append(newInterval)
                newInterval = intervals[i]
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        merge.append(newInterval)
        return merge