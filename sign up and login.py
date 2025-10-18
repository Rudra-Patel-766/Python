import random
OTPs=[1234,6784,8926,1020,6677,2254,3035,1896]

print("Create Your account by doing sign up")

a=input("Username: ")
b=input("Password: ")
c=input("Phone Number: ")
d=input("Email: ")

print("Now Verify OTP")
s=0
while True:
    s+=1
    otp=random.choice(OTPs)
    print(f"OTP recived on email is: {otp}")    

    email_otp=int(input("Enter otp recived on email: "))
    print(email_otp)
        
    if otp==email_otp:
        print("Now Login to your account")
        break
    else:
        print("Wrong OTP")

i=0
while True:
    i+=1
    login_details=[a,b,c,d]
    Username=input("Username: ")
    Password=input("Password: ")
    if Username==login_details[0] and Password==login_details[1]:
        print("Login successful")
        break
    else:
        print("Wrong login details")