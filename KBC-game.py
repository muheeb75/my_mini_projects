questions=['Who developed Pyhtho language?',
           'Who developed JAVA language?',
           'Who developed C++ language?',
           'Who developed C language?',
           'What is e-zin?',
           'Expandation of ASCII?',
           'What is NIC?',
           'What is Tic-Tac-Toe?',
           'Which famous web site was found by Jeffre Bezos?',
           'In which year Microsoft office was launched?',
          
           ]

answers=['Guido Van Rossum',
           'James Gosling',
           'Bjarne Stroustrup',
           'Dennis Ritchie',
           'Electronic Magazines',
           'American Standard Code for Information Interchange',
           'Network Interface Card',
           'First graphical game',
           'Amazon.com',
           '1989',

           ]

options=[['Guido Van Rossum','James Gosling','Bjarne Stroustrup','Dennis Ritchie'],
           ['Dennis Ritchie','Bjarne Stroustrup','James Gosling','Guido Van Rossum'],
           ['Bjarne Stroustrup','Guido Van Rossum','Dennis Ritchie','James Gosling'],
           ['Bjarne Stroustrup','Dennis Ritchie','Guido Van Rossum','James Gosling'],
           ['Electronic Materials','Electronic Memories','Electronic Magazines','Electronic Machines'],
           ['American Standard Code for Information Internet','Asia Standard Code for Information Interchange','American Step Code for Information Interchange','American Standard Code for Information Interchange'],
           ['Network Internet Card','Network Interface Ccode','Network Internet Code','New Interface Card'],
           ['largest graphical game','smallest graphical game','First graphical game','Second graphical game'],
           ['Amazon.com','Flipcart.com','Superkit.com','Minimarket.com'],
           ['1985','1999','1989','1969']

           ]

def play_game(username,questions,answers,options):
    print('Welcome MR.',username,"to Our game!")
    score=0
    
    for i in range(len(questions)):                                      
        current_question = questions[i]
        correct_answer = answers[i]
        current_options = options[i]
        print("Question :",current_question)
        for j,k in enumerate(current_options):
            print(j,":",k)
        index=int(input("Enter your option : "))
        
        user_answer = current_options[index]
        
        if(user_answer == correct_answer):
            print("Correct answer!")
            score = score + 100
        else:
            print("Wrong answer")      
                
    print("Final score : ",score)
    return username,score

def view_score(name_and_score):
    for name,score in name_and_score.items():
        print(name,"has scored",score)
        
def main_pro(questions,answers,options):
    name_and_score={}
    while True:
        print("1) Play Game\n2) View Score\n3) Exit")
        choice=int(input("Enter your choice : "))
        if choice == 1:
            username=input("Enter your name : ")
            username,score = play_game(username,questions,answers,options)
            name_and_score[username] = score
        elif choice == 2:
            view_score(name_and_score)
        elif choice == 3:
            exit(0)
        else:
            print("Invalid entry please try again")
main_pro(questions,answers,options)            
            
            
    
