n_terms = int(input ("How many terms the user wants to print? "))  
  # fibnocci series of numbers
# First two numbers 
n_1 = 0  
n_2 = 1  
count = 0#initialis count  
  
# Then we will generate Fibonacci sequence of number
if n_terms <= 0:  
    print ("Please enter a positive integer, the given number is not valid")  

elif n_terms == 1:  
    print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
    print(n_1)
    Print("computing")  
# if there is only one term, it will return n_1  
else:  
    print ("The fibonacci sequence of the numbers is:")  # Now, we will check if the number of terms is valid or not  
    while count < n_terms:  
        print(n_1)  
        nth = n_1 + n_2  
       # At last, we will update values  
        n_1 = n_2  
        n_2 = nth  
        count += 1  
#EOF
print("the program interpreted successfully")
