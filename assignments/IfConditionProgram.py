# num = int(input("Enter your number:"))
# if num > 0:
#     print("Positive number")
# elif num < 0:
#     print("Negative number")
# else :
#     print("Zero")

# age = int(input("Enter your age:"))
# if age >= 18:
#     print("You can vote")
# if age >= 21:
#     print("You can drink alcohol (in US)")
# print("Thank you")

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

    

# hours = 2
# mintus = 30
# seconds = 45
# total_seconds = (hours*3600) + (mintus * 60) + seconds
# print("Total seconds:", total_seconds)

number = 456
ones = number % 10 
tens = (number // 10) % 10 
hundreds = number // 100

print("Hundreds:", hundreds, ", Tens:", tens, ", Ones:", ones)