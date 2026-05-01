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
    # The program will only be ended if inputed age is under 13 since this is all indented
time.sleep(2)
q1 = "Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?"
print(q1)
time.sleep(3)
print("a. Delete the message and try to forget about it")
time.sleep(1.3)
print("b. Keep the text and show an adult you trust")
time.sleep(1.3)
print("c. Text the person back saying something mean to them")
time.sleep(.5)
print("A B, or C")
a1 = input()
if a1 == "B":  
    print ("good job")
    points += 10 
points = str(points)
print("Well done you have " + str(points) + " points thats alot!")















