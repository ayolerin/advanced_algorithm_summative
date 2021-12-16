# Ayo-Fisher Oluwapamilerin 
# Question 4
# This program will allow the user find the super digit of an integer; 

# create the digit_sum function that takes the super_digit as an argument 
def digit_sum(super_digit):
    # create the num_sum variable to store 
    # the present sum of the numbers and store it as zero 
    num_sum = 0
    # for loop to loop through numbers given 
    for number in super_digit:
        # increment the sum variable by the numbers given  
        num_sum = num_sum + int(number)
        # return the num_sum variable 
    return str(num_sum)

# create the superDigit function that takes n and k as arguments 
def superDigit(n, k):
    # create the super_digit variable to 
    # store the multiplied value of the digit_sum variable by k 
    super_digit = digit_sum(n)*k
    # if statement to check if the the length of the integer is 1 
    if len(super_digit) == 1:
        # return the super_digit variable if the length of the integer is 1
        return str(super_digit) 
    # else statement if the length of the integer is not 1
    else:
    # return the superDigit function 
        return str(superDigit(super_digit, 1))
        
 
# test cases
n = '9875'
k = 4
p = str(n*k)
print("n = " + str(n))
print("k = " + str(k))
print("p = " + str(p))
print("super digit = " + str(superDigit(n,k)))

print(" ")

n = '148'
k = 3
p = str(n*k)
print("n = " + str(n))
print("k = " + str(k))
print("p = " + str(p))
print("super digit = " + str(superDigit(n,k)))
