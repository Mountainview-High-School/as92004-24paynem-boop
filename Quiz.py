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
#loop needs to be implemented here.
questions = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?", "You find out somebody has posted an embarrassing picture of you online. What should you do?", "You want to join an online gaming site. Which of the following infomation is okay for you to post on the site"]
qno = 0 
print(questions[qno])
choices = ["a. Delete the message and try to forget about it", "b. Keep the text and show an adult you trust", "c. Text the person back saying something mean to them" ]
print(choices[qno])
time.sleep(.5)
print(choices[qno +1])
time.sleep(.5)
print(choices[qno +2])
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
print(questions[1])
print(questions[2])


print("Well done you have " + str(points) + " points thats alot!")