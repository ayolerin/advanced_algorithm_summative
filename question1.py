# Ayo-Fisher Oluwapamilerin 
# Question 1
# This program will allow the user to return the sum of the first n numbers; 
# import the time function
import time
# create the input_sum(n) function to store the inputs
def input_sum(n):
    # create the current variable, to store the present sum of numbers
    current = 0
    
    # for loop to loop the range of numbers 
    # start from first index till the last index
    for integers in range(1,n+1):
        # increment the current variable with the present index 
        current = current + integers
        
    # return the current variable
    return current
    
# Testcases     
begin = time.process_time()
final = time.process_time() - begin
# print the sum and the time taken for each input value 
print("Given input 10, the output is "+ str(input_sum(10)) + '. The time taken for the input of 10 is ' + str(final)+"secs")
print("Given input 10000, the output is "+ str(input_sum(10000)) + '. The time taken for the input of 10000 is ' + str(final)+"secs")
print("Given input 1000000, the output is "+ str(input_sum(1000000)) + '. The time taken for the input of 1000000 is ' + str(final)+"secs")
print("Given input 1000000000, the output is "+ str(input_sum(1000000000)) + '. The time taken for the input of 1000000000 is ' + str(final)+"secs")

