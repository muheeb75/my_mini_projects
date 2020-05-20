import random
def game2():
    count=0
    name=input("Enter your name : ")
    print("Welcome ",name,"to our big-bang game\n")
    print("Rules of the big-bang game :\n")
    print("1.You will get 3 input chances in that 2 input should mach then you will be the winner")
    print("2.You can enter the number between 0-9")
    print("3.For each correct input you will get 100 points ")
    print("4.After the end of the game your score will be displayed\n")
    print("To start the game please enter your number and press enter\n")   
    for i in range(3):
        number=int(input("Enter your number : "))
        if number>=9:
            print("Please enter correct number according to the rule")
        else:
            n=random.randint(0,1)
            if number==n:
# function to print random number -> print(random.randint(0,9))
                print("Congrats our big-bang number is mached with your given number!")
                count=count+100
            else:
                print("badluck! the number was ",n)
                if i==0:
                    print("Second chance")
                elif i==1:
                    print("Last chance")
                    continue
           


    print("The Final score is ",count,"\n")
    if count==200:
        print("Congratulations you are the winner of our big-bang game!!!")
    else:
        print("You have scored",count,"out of",300)
        print("Betterluck next time")
        
game2()
