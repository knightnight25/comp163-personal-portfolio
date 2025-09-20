full_name = "Jordan Smith"
student_email = "jsmith@ncat.edu"
hometown = "Charlotte, NC"
graduation_semester = "Spring 2028"
major = "Computer Science"

current_courses = ["COMP 163", "MATH 150", "ENG 101", "HIS 105"]
completed_courses = ["Biology", "Chemistry", "Calculus", "Spanish II", "World History"]
credit_hours = {"COMP 163": 3, "MATH 150": 3, "ENG 101": 3, "HIS 105": 3}
gpa_history = [3.2, 3.6, 3.4, 3.7]

emergency_contact = ("Mom", "Hannah Smith", "704-555-0199")
home_address = ("456 Oak Street", "Charlotte, NC", "28202")
instagram_info = ("Instagram", "@jordan_codes", 312)
twitter_info = ("Twitter", "@jordandev", 127)
birthday = ("Birthday", "5", "22", "2006")

current_skills = {"Python basics", "HTML", "Problem solving", "Time management", "Photography"}
skills_to_learn = {"JavaScript", "Data structures", "Git", "Web design", "Public speaking"}
career_interests = {"Software development", "Web development", "Data science", "Game development"}
hobbies = {"Gaming", "Photography", "Reading", "Soccer", "Music"}
entertainment_backlog = {"One Piece", "Barry", "Life", "Incantation", "Memento"}

course_professors = {"COMP 163": "Prof. Rhodes", "MATH 150": "Dr. Lee", "ENG 101": "Dr. Martinez", "HIS 105": "Dr. Brown"}
course_rooms = {"COMP 163": "M-Eric 300", "MATH 150": "Marteena 201", "ENG 101": "Crosby 121", "HIS 105": "Crosby 210"}
monthly_budget = {"Food": 450, "Entertainment": 200, "Books": 125, "Transportation": 100}
study_hours_per_subject = {"Programming": 10, "Math": 8, "English": 4, "History": 3}
contact_directory = {"Mom": "704-555-0199", "Roommate": "336-555-7821", "Academic Advisor": "336-334-5000"}

total_credits = sum(credit_hours.values())
cumulative_gpa = round((sum(gpa_history) / 4), 2)
completed_course_count = len(completed_courses)
total_study_hours = sum(study_hours_per_subject.values())
academic_load = total_credits + total_study_hours
total_monthly_budget = sum(monthly_budget.values())
daily_food_budget = round(monthly_budget.get("Food", 0) / 30, 2)
annual_budget_projection = total_monthly_budget * 12
study_cost_per_hour = round(monthly_budget.get("Books", 0) / total_study_hours, 2)

total_followers = twitter_info[2] + instagram_info[2]

print("================================================================")
print("                 PERSONAL ACADEMIC & LIFE PORTFOLIO")
print("================================================================")
print(f"Student: {full_name} | Email: {student_email}")
print(f"From: {hometown} | Graduating: {graduation_semester}")
print(f"Major: {major}\n")

print("=== ACADEMIC PROFILE ===")
print(f"Current Semester: {total_credits} credits across {len(current_courses)} courses")
print(f"Cumulative GPA: {cumulative_gpa}")
print(f"Weekly Study Time: {total_study_hours} hours")
print(f"Academic Investment: ${study_cost_per_hour} per study hour\n")

print("Current Courses:")
print(f"{current_courses[0]} - {credit_hours["COMP 163"]} credits - {course_professors["COMP 163"]} - {course_rooms["COMP 163"]}")
print(f"{current_courses[1]} - {credit_hours["MATH 150"]} credits - {course_professors["MATH 150"]} - {course_rooms["MATH 150"]}")
print(f"{current_courses[2]} - {credit_hours["ENG 101"]} credits - {course_professors["ENG 101"]} - {course_rooms["ENG 101"]}")
print(f"{current_courses[3]} - {credit_hours["HIS 105"]} credits - {course_professors["HIS 105"]} - {course_rooms["HIS 105"]}")
print()

print("=== PERSONAL DEVELOPMENT ===")
print(f"Current Skills: {current_skills}")
print(f"Learning Goals: {skills_to_learn}")
print(f"Career Interests: {career_interests}")
print(f"Skills Currently Have: {len(current_skills)}")
print(f"Skills Want to Learn: {len(skills_to_learn)}\n")

print("=== FINANCIAL OVERVIEW ===")
print(f"Monthly Budget: ${total_monthly_budget}")
print(f"Food: ${monthly_budget.get('Food', 0)} (${daily_food_budget}/day)")
print(f"Entertainment: ${monthly_budget.get('Entertainment', 0)}")
print(f"Books: ${monthly_budget.get('Books', 0)}")
print(f"Transportation: ${monthly_budget.get('Transportation', 0)}")
print(f"Annual Projection: ${annual_budget_projection}\n")

print("=== CONNECTIONS & CONTACTS ===")
print(f"Emergency Contact: {emergency_contact[1]} ({emergency_contact[0]}) - {emergency_contact[2]}")
print(f"Home Address: {home_address[0]}, {home_address[1]} {home_address[2]}")
print(f"Social Media Presence: {total_followers} followers across 2 platforms")
print(f"Key Contacts: {len(contact_directory)} people in directory\n")

print("=== LIFE STATISTICS ===")
print(f"Total Courses Completed: {completed_course_count}")
print(f"Current Academic Load: {academic_load} weekly commitments")
print(f"Entertainment Backlog: {len(entertainment_backlog)} items")
print(f"Current Hobbies: {len(hobbies)} activities")
print("================================================================")