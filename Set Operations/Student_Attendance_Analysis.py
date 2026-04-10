# Sample sets of student roll numbers for two days
day1 = {101, 102, 103, 104, 105}
day2 = {104, 105, 106, 107}

# 23. Students present on both days (intersection)
present_both_days = day1.intersection(day2)

# 24. Students present on either day (union)
present_either_day = day1.union(day2)

# 25. Students absent on the second day
# Assuming the full list of students is those who attended on day 1 and/or day 2
all_students = day1.union(day2)
absent_on_day2 = day1.difference(day2)  # Students in day1 but not in day2

print("Students present on both days:", present_both_days)
print("Students present on either day:", present_either_day)
print("Students absent on the second day:", absent_on_day2)
