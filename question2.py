# Ayo-Fisher Oluwapamilerin 
# Question 2
# This program will allow the user to return the grades after rounding as appropriate; 
# import the math library
import math

# create the student_grade(grade) function to store the students grades
def student_grade(n):
    # create the  grade_final array to store the final grades after rounding 
    grade_final = []
    
    # for loop to loop through each grade in the grade_original array
    for n in grade_original:
        # if statement to check for any grade in the grade_original arrY is < 38
        if n < 38:
            # adding the grade as it is to the grade_final array as it < 38 and no rounding is needed
            grade_final.append(n) 
        
        # else statement to round the grades in the grade_original array is >= 38
        else:
            # create a variable called final that stores the divition of the
            # grade by 5 and rounds it to the nearest whole number  
            final = math.ceil(n/5)
            # create a rounded_grade variable to multiply the final variable by 5
            rounded_grade = final * 5
            
            # create a variable called new that stores the difference between '
            # the rounded grade and the original grade
            new = rounded_grade - n
             # if statement to make sure the new variable has a difference of <3
            if new < 3:
                # append the rounded grade to the rounded_grade array 
                grade_final.append(rounded_grade)
            # else statement for the new variable with a difference of >=3 
            else:
                # addind the grade as it is to the grade_final array as 
                # the new variable has a difference of >= 3  
                grade_final.append(n)
                
    # return the grade_final array 
    return grade_final

# Test case 
grade_original = [73,67,38,33]

print("Original Grades For Students 1, Student 2, Student 3 and Student 4 are: "+ str(grade_original)+ " respectively.")
print("Rounded Grades For Students 1, Student 2, Student 3 and Student 4 are: "+ str(student_grade(grade_original))+ " respectively.")
