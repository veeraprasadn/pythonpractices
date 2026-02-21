# 1)Takes a number as input
# If the number is positive (> 0), print "Positive number"
# If the number is negative (< 0), print "Negative number"
# If the number is zero (== 0), print "Zero"
# Example:

# Enter a number: 5
# Positive number
# num = int(input("Enter your number:"))
# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else :
#     print("Zero")

Takes user's age as input
If age is 18 or above, print "You can vote"
If age is 21 or above, print "You can drink alcohol (in US)"
Always print "Thank you" at the end
Example:

#2) Enter your age: 25
# You can vote
# You can drink alcohol (in US)
# Thank you
# age = int(input("Enter your age:"))
# if age >= 18:
#     print("You can vote")
# if age >= 21:
#     print("You can drink alcohol (in US)")
# print("Thank you")

# 3)Take a score (0-100) as input
# Use multiple if statements to:
# Check if score >= 90: print "Grade: A" and "Excellent work!"
# Check if score >= 80 and < 90: print "Grade: B" and "Good job!"
# Check if score >= 70 and < 80: print "Grade: C" and "Satisfactory"
# Check if score >= 60 and < 70: print "Grade: D" and "Needs improvement"
# Check if score < 60: print "Grade: F" and "Failed"
# Also check:
# If score == 100: print "Perfect score!"
# If score < 50: print "Please see instructor"
# Example:

# Enter your score: 95
# Grade: A
# Excellent work!
# Hint: You'll need multiple if statements with different conditions!

# score = int(input("Enter your score:"))
# if score>= 90:
#     print("Grade: A")
#     print("Excellent work!")
# if score >= 80 and score < 90:
#     print("Grade: B")
#     print("Good job!")
# if score >= 70 and score < 80:
#     print("Grade: C")
#     print("Satisfactory")
# if score >= 60 and score < 70:
#     print("Grade: D")
#     print("Needs improvement")
# if score < 60 and score < 70:
#     print("Grade: F")
#     print("Failed")
# if score == 100:
#     print("Perfect score!")
# if score < 50:
#     print("Please see instructor")
# 4. Movie Ticket Pricing
# Calculate movie ticket price based on age and student status:

# Child (under 18) student: $5
# Child non-student: $7
# Adult (18+) student: $8
# Adult non-student: $10
# Test with age = 15, is_student = True.

# Expected Output:

# Ticket price: $5
# Hint: Outer if checks age, inner if checks student status for each age group.
# age = 15
# is_student = True
# if age < 18:
#     if is_student:
#         print("Ticket price: $5")

#     else:
#         print("Ticket price: $7")
# if age >= 18:
#     if is_student:
#         print("Ticket price: $8")

#     else:
#         print("Ticket price: $10")
# 5. Login Validation
# Write a login system that checks:

# Is username provided?
# Is password provided?
# Does username match "admin"?
# Does password match "secret123"?
# Provide specific error messages for each failure point.

# Test with username = "admin", password = "secret123".

# Expected Output:

# Login successful
# Hint: Use 4 levels of nesting, one for each check. Provide specific error in each else.
# username = "admin"
# password = "secret123"

# if username:  # Check if username is provided
#     if password:  # Check if password is provided
#         if username == "admin":  # Check if username matches
#             if password == "secret123":  # Check if password matches
#                 print("Login successful")
#             else:
#                 print("Error: Incorrect password")
#         else:
#             print("Error: Invalid username")
#     else:
#         print("Error: Password not provided")
# else:
#     print("Error: Username not provided")
# 6. Create a tip calculator:
# Bill amount: $85.00
# Tip rate: 18%
# Calculate tip amount
# Calculate total
# Split among 4 people

# bill_amount = 85.00 
# tip_rate = 0.18 
# people = 4

# tip_amount = bill_amount * tip_rate
# total_amount = bill_amount + tip_amount
# split_amount = total_amount / people

# print("Bill amount: $" + str(bill_amount)) 
# print("Tip amount: $" + str(round(tip_amount, 2))) 
# print("Total amount: $" + str(round(total_amount, 2))) 
# print("Each person pays: $" + str(round(split_amount, 2)))

# 7. Convert hours to total seconds:
# Input: 2 hours, 30 minutes, 45 seconds
# Output: total seconds
# Formula: (hours × 3600) + (minutes × 60) + seconds    

# hours = 2
# mintus = 30
# seconds = 45
# total_seconds = (hours*3600) + (mintus * 60) + seconds
# print("Total seconds:", total_seconds)
# 8. Write a program that:
# Takes a 3-digit number (e.g., 456)
# Extracts each digit using % and //
# Prints: "Hundreds: 4, Tens: 5, Ones: 6"
# Hint:

# Ones: number % 10
# Tens: (number // 10) % 10
# Hundreds: number // 100

number = 456
ones = number % 10 
tens = (number // 10) % 10 
hundreds = number // 100

print("Hundreds:", hundreds, ", Tens:", tens, ", Ones:", ones)
