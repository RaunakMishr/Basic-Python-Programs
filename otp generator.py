#otp generator 
import random as r
len1 = int(input('Enter length of the otp you want: (8-12 digits)'))
otp = str(r.random())
s = otp[2:len1+2]
s = int(s)
print('Your OTP is: ',s)


 #second method

import math as m

  
# function to generate OTP 
def OTPgen() : 
  
    # Declare a string variable   
    # which stores all alpha-numeric characters 
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = "" 
    varlen= len(string) 
    for i in range(6) : 
        OTP += string[m.floor(r.random() * varlen)] 
  
    return (OTP) 
  
# main function 
if __name__ == "__main__" : 
      
    print("Your One Time Password is ", OTPgen())