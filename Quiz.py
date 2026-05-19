import time
import sys
points = 0 
print("What is your name?")
username = input()
print("Hello, " + username + " What is your age?")
age = input()
age = int(age)
if age > 13:
    print("It is recommended that you try the Cybersmart youth Quiz instead of this one") 
    time.sleep(2)
    sys.exit("Ending program")
    # The program will only be ended if inputed age is over 13 since this is all indented
time.sleep(.5)
print ("Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?")
choices1 = ["a. Delete the message and try to forget about it", "b. Keep the text and show an adult you trust", "c. Text the person back saying something mean to them" ]
print(choices1[0])
time.sleep(.5)
print(choices1[1])
time.sleep(.5)
print(choices1[2])
time.sleep(1)
print("Input : A, B or C")
i=0
while i<3:
    print (i)
    a1 = input()
    if  a1 == "B" or a1 =="b":  
        print ("good job") 
        if i ==0: points += 10
        break 
    else :
         print("Incorrect") 
    i += 1
print("Loop Ended")

print("Well done you have " + str(points) + " points thats alot!")