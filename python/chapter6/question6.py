# write a program to calculate the grade of a student from his marks from the following scheme:
# 90-100=>Ex
# 80-90=>A
# 70-80=>b
# 60-70=>C
# 50-60=>D
# <50=>F 
marks = int(input("enter your marks here :"))
if(marks<=100 and marks>=90):
    grade = "ex"
elif(marks<90 and marks>=80):
    grade = "a"
elif(marks<80 and marks>=70):
    grade = "b"
elif(marks<70 and marks>=60):
    grade = "c"
elif(marks<60 and marks>=50):
    grade = "d"
elif(marks<50):
    grade = "f"
print(grade)
