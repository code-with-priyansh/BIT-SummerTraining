#1. write a program to check weather a number is positive negative or zero

num= int(input("enter a number"))

if num>0:
    print("number is possitive")
elif num<0:
    print("number is negative")
else:
    print("number is zero")

# 2. write a program to check whether a number is even or odd.

num = int(input("enter the number"))

if num % 2==0:
    print(f"{num} number is even")
else:
    print(f"{num} number is odd")    

# 3.create a list 10 number and print each number using a loop.

numbers = [10,20,30,40,22,33,44,55,66,77]
print("list number")
for num in numbers:
    print(num)

# 4.write a function named calculate_average that task 3 mark and return the average.

def calculate_average (m1,m2,m3):
 total = m1+m2+m3
 average = total/3
 return average

mark1=40
mark2=50
mark3=80

result =calculate_average(mark1,mark2,mark3)
print(f"three number avrage:{result}")

#5. Write a function named  grade_student that prints a grade based on marks.

def grade_student(mark):
    if not (0 <= mark <= 100):
        print("invalid.mark.please enter a value between 0 and 100")
    elif mark >= 90:
        print("Grade: A")
    elif mark >= 80:
        print("Grade: B")
    elif mark >= 70:
        print("Grade: C")
    elif mark >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

grade_student(85)