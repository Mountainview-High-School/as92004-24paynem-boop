
import time, sys 
points = 0 
print("What is your name?")
correcta = ["B", "b", "C", "c", "A", "a"]   
questions = ["Someone sends you a text that is hurtful and makes you feel bad about yourself. What should you do?", "You find out somebody has posted an embarrassing picture of you online. What should you do?", "You want to join an online gaming site. Which of the following infomation is okay for you to post on the site"]
choices = ["a. Delete the message and try to forget about it", "b. Keep the text and show an adult you trust", "c. Text the person back saying something mean to them", "a. Tweet that they are an idiot and a loser", "b. Ask your friends to give the person a hard time", "c. Tell an adult you trust", "a. A nickname", "b. Your name", "c. Your email address", ]

username = input()
usernamec = username.capitalize()
#if the inputed name is micah it will convert it to Micah because it capitalizes the first letter, it also makes all the other letters undercase so if the input was mICAH it would also be converted to Micah 
print("Hello, " + usernamec + " What is your age?")

age = input()
while age.isnumeric() == False: 
    print("Invalid try again")
    age = input()
age = int(age)
#the float allows the inputed age to include decimals so numbers like 12.3 or 1.3 can be inputed not just the whole numbers.
if age > 13:
    print("It is recommended that you try the Cybersmart youth Quiz instead of this one") 
    time.sleep(2)
    sys.exit("Ending program")
    # The program will only be ended if inputed age is over 13 since this is all indented
if age < 8:
    print("It isnt recommended that you attempt this quiz due to your age being to low")
    time.sleep(2)
    sys.exit("Ending program")
    #program ends if inputed age is lower than 8 
time.sleep(1)
#loop needs to be implemented here.
qno = 0 
l=0
while l<3:
    print
    print(questions[qno])
    cno = qno * 3 
    time.sleep(2)
    print(choices[cno])
    time.sleep(1)
    print(choices[cno +1])
    time.sleep(1)
    print(choices[cno +2])
    time.sleep(1)
    i=0
    l += 1 
    while i<3:
        print("Input : A, B or C")
        a1 = input()
        if  a1 == correcta[qno*2] or a1 == correcta[qno*2+1]:
            #this checks if correct input has been inputed or not
            print ("good job") 
            if i ==0: points += 10
            #this chicks if the first attempt at the question was right they get 10 points, if it was their second or third they will not receive any points
            break 
        else :
            print("Incorrect") 
        i += 1
    print("Loop Ended")
    time.sleep(2.5)
    qno += 1 
print("Well done, you have " + str(points) + " good job!")
 