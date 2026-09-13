# TASK :
# Create dictionary of 3 students with marks:
# - Rahul → 85
# - Priya → 90
# - Rohan → 65

# Loop and print:
# - marks > 75 → "Pass"
# - marks < 75 → "Fail"

# Expected Output:
# Rahul - Pass
# Priya - Pass
# Rohan - Fail

# 1. Create the dictionary
student_marks = {
    "Rahul": 85, 
    "Priya": 90, 
    "Rohan": 65
}

# 2. Loop through the dictionary items (Name and Mark)
for name, mark in student_marks.items():
    # 3. Check the condition for each student
    if mark >= 75:
        print(f"{name} - Pass")
    else:
        print(f"{name} - Fail")


# Key Improvements.items(): 
# This method lets you look at bot  the key (name) and the value (mark) at the same time inside the loop.
# No Function Needed: For a simple script like this, you don't need to wrap the dictionary inside a def marks() function unless specifically requested by an assignment.