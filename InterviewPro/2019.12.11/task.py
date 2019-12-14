'''
You are given an array of tuples (start, end) representing time intervals for lectures. The intervals may be overlapping. Return the number of rooms that are required.

For example. [(30, 75), (0, 50), (60, 150)] should return 2.
'''

def rooms_number(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    rooms = [0]
    for interval in sorted_intervals:       
        to_book = -1 
        min_time = -1
        for i in range(len(rooms)):
            room = rooms[i]
            waiting_time = interval[0] - room
            if waiting_time >= 0 and (min_time == -1 or waiting_time < min_time):
                min_time = waiting_time
                to_book = i

        if to_book != -1:
            rooms[i] = interval[1]
        else:
            rooms.append(interval[1])

    return len(rooms)

print(rooms_number([(30, 75), (0, 50), (60, 150)]))

