# Ayo-Fisher Oluwapamilerin 
# Question 3
# This program will allow the user to encrypt and decrypt messages; 
# import the time function
import time 

# Create the text variable to store the text 
text_var = 'Plain text'
# Create the key variable to store the key
key_var = 3


# create the encrypt(text_var,key_var) function with the text_var and key_var as arguments 
def encrypt(text_var,key_var):
    # create the e_mess variable to store the encrypted message 
    e_mess = ""

    # create the begin variable to start and stop according to the key_var
    begin = 0
    

    # while loop to loop through the begin variable when less than the key_var
    while begin < key_var:
        # for loop to loop through the lenght of the text_var using the key_var
        for thing in range(begin,len(text_var),key_var):
            # increment the e_mess variable with the text_var 
            e_mess = e_mess + text_var[thing]
        # increment the begin variable to make the steps 
        # equal the key_var starting from the next index 
        begin = begin + 1

    # return the e_mess variable 
    return e_mess

# call the encrypt function 
eted = encrypt(text_var,key_var)
 


# create the decrypt(text_var,key_var) function with the eted and key_var as arguments 
def decrypt(eted,key_var):
    # create the stuff variable and set it to 0
    stuff = 0
    # create the d_mess variable to store the decrypted messagea
    d_mess = ''
    
    # if statement to check when both the length of the text and key are even 
    if len(eted) % 2 == 0 and key_var % 2 == 0: 
        # create the mach variable to divide the lenght of the eted variable by the key_var 
        mech = len(eted)//key_var 
        
        # while loop to loop through the stuff variable when less than the mech
        while stuff < mech:
            # for loop to loop through the lenght of the text 
            # starting from stuff and take mech steps each time
            for good in range(stuff,len(eted),mech):
                # increment the d_mess variable with eted[good]
                d_mess = d_mess + eted[good]
            # increment the stuff variable 
            stuff = stuff + 1 
            
    # if statement to check when the lenght of the text is even but the key is odd 
    if len(eted) % 2 == 0 and key_var % 2 != 0:
        # update the mech variable to divide the lenght of the eted variable by the key_var
        mech = len(eted)//key_var 
        
        # while loop to loop through the stuff variable when less than the mech 
        while stuff < mech:
            # increment the mech variable 
            mech = mech + 1
            # increment the d_mess variable by the eted[stuff]
            d_mess = d_mess + eted[stuff] 
            # for loop to loop through the length the word starting at good variable 
            for good in range(stuff,len(eted)):
                # create the hold variable to store the sum of the good and mech variable 
                hold = good + mech
                # increment the d_mess variable with the eted[hold]
                d_mess = d_mess + eted[hold]
                # increment the d_mess variable by the eted[hold+key_var]
                d_mess = d_mess + eted[hold+key_var]
                # break the loop 
                break
                
            # update the mech variable to divide the lenght of the eted variable by the key_var
            mech = len(eted)//key_var 
            # increment the stuff variable 
            stuff = stuff + 1 
        # increment the d_mess variable by the eted[mech]
        d_mess = d_mess + eted[mech]

    # return the d_mess variable
    return d_mess

# call the decrypt function 
dect = decrypt(eted,key_var)

start = time.process_time()
print("Text: " + text_var + " & Key: " + str(key_var))
print("Encrypted message: "+ eted + ". Decrypted message: " + dect)
print("With the key " + str(key_var) + ". The time taken is " + str(time.process_time() - start)+"secs" )
