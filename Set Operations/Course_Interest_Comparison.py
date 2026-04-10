# Sample course interests for two users
user1_courses = {"Python", "Data Science", "Machine Learning", "SQL"}
user2_courses = {"Data Science", "Cybersecurity", "Python", "Cloud Computing"}

# Find common interests (intersection)
common_interests = user1_courses.intersection(user2_courses)

# Suggest new courses to user1 based on user2's interests (difference)
suggested_courses_for_user1 = user2_courses.difference(user1_courses)

print("Common interests between users:", common_interests)
print("Courses suggested to User 1 based on User 2's interests:", suggested_courses_for_user1)
