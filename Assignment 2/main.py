# Student Name & Marks
name = "Mohammad Saad"
math = 85
english = 90
urdu = 92
chemistry = 90
computer =  96
print("Name: " + name)
print("Maths: " + str(math))
print("English: " + str(english))
print("Urdu: " + str(urdu))
print("Chemistry: " + str(chemistry))
print("Computer: " + str(computer))

# Total Obtained Marks
obtainedmarks = math + english + urdu + chemistry + computer

# Total Marks
totalmarks = 500
print("Total: " + str(obtainedmarks) + "/" + str(totalmarks))

# Percentage
percentage = (obtainedmarks / totalmarks) * 100
print("Percentage: " + str(percentage))

# Grade Condition
if percentage >= 90:
    print("Grade: A+")
elif percentage >= 80 and percentage <= 89:
    print("Grade: A")
elif percentage >= 70 and percentage <= 79:
    print("Grade: B+")
elif percentage >= 60 and percentage <= 69:
    print("Grade: B")
else:
    print("Grade: C")