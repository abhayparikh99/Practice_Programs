# Game zone....
import random

# Write a program for Rock_Paper_Scissors game.
# user/computer  will get 1 point for winning, Play game until user/computer score=3 point.
class RPS():
    user_score=0
    computer_score=0

    def __init__(self):
        print("Welcome to 'Rock Paper Scissors'".center(130)) ;print()
        print("Instruction :\nRock smashes scissors, so in this case Rock get 1 point.\nPaper covers rock, so in this case Paper get 1 point.\nScissors cut paper, so in this case Scissor get 1 point.")
        print("Use notation:\n'r' for 'rock' \n'p' for 'paper' \n's' for 'scissor'\n")
    def play_RPS(self,user_score,computer_score):
        status=True
        while status:   #loop will continue until any of user score becomes 3. # or score==3 then break.
            print("---> Enter Your Choice")
            user_choice=input("User Choice is:")
            tickets=['r','s','p']
            computer_choice=random.choice(tickets)
            print("Computer Choice is:",computer_choice);print()
            if user_choice in ["r","s","p"]:
                if user_choice!=computer_choice:
                    if user_choice=='r': 
                        if computer_choice=='s':
                            print("User Won!! Rock smashes scissor.")
                            user_score+=1
                            print("User Current Score is:",user_score) #or user_choice=='s' and computer_choice=='p':
                            print("Computer Current Score is:",computer_score);print()
                        else:
                            print("Computer Won!! Paper covers rock.")
                            computer_score+=1
                            print("User Current Score is:",user_score)
                            print("Computer Current Score is:",computer_score);print()
                    
                    if user_choice=='s':
                        if computer_choice=='p':
                            print("User Won!! Scissor cut paper.")
                            user_score+=1
                            print("User Current Score is:",user_score)
                            print("Computer Current Score is:",computer_score);print()
                        else:
                            print("Computer Won!! Rock smashes scissor.")
                            computer_score+=1
                            print("User Current Score is:",user_score)
                            print("Computer Current Score is:",computer_score);print()
                    
                    if user_choice=='p':
                        if computer_choice=='r':
                            print("User Won!! Paper covers rock.")
                            user_score+=1
                            print("User Current Score is:",user_score)
                            print("Computer Current Score is:",computer_score);print()
                        else:
                            print("Computer Won!! Scissor cut paper.")
                            computer_score+=1
                            print("User Current Score is:",user_score)
                            print("Computer Current Score is:",computer_score);print()

                else: 
                    print("Tie!!!");print()
            else:
                print("Invalid Choice");print()
            if user_score==3 or computer_score==3:
                status=False
        print("Total Score of User is:",user_score)
        print("Total Score of Computer is:",computer_score)
        if user_score>computer_score:
            print("User Won the Game!!")
        else:
            print("Computer Won the Game!!")

# WAP to create Housie Game.
class HG():
    main_ticket=[]
    user_ticket=[]
    computer_ticket=[]
    def play_housie(self):
        self.n=int(input("Enter Number from which you want genertae tickets :"))

        #Code for Generate  main_ticket.
        print("Tickets are :",end=" ")
        status=True
        while status:
            ran=random.randint(1,99)
            if ran not in self.main_ticket:
                self.main_ticket.append(ran)
            if len(self.main_ticket)==12:
                status=False
        for i in self.main_ticket:
            print(i,end=" ")
        print();print()
        
        #Code for Generate user_ticket.
        print("User's Tickets are :",end=" ")
        for i in self.main_ticket:
            u_ran=random.choice(self.main_ticket)
            if u_ran not in self.user_ticket:
                self.user_ticket.append(u_ran)
            if len(self.user_ticket)==6:
                break
        for i in self.user_ticket:
            print(i,end=" ")
        print();print()
        
        #Code for Generate computer_ticket/
        print("Computer's Tickets are :",end=" ")
        for k in self.main_ticket:
            if k not in self.user_ticket:
                self.computer_ticket.append(k)
        for i in self.computer_ticket:
            print(i,end=" ")
        print();print()
        
        #Code for Open one by one tickets and check in which those ticket is present and 
        # then remove from those list and print new list.
        for i in self.main_ticket:
            print("Entered Value is :",i)
            if i in self.user_ticket:
                self.user_ticket.remove(i)
                print("Removed value from user's Ticket is :",i)
                print("Remaining Values in user's Ticket are :",self.user_ticket)
                self.element=input()
                if len(self.user_ticket)==0:
                    print("User is win this Game!!!")
                    break
            elif i in self.computer_ticket:
                self.computer_ticket.remove(i)
                print("Removed value from computer's Ticket is :",i)
                print("Remaining values in computer's Ticket are :",self.computer_ticket)
                self.element=input()
                if len(self.computer_ticket)==0:
                    print("Computer is win this Game!!!")
                    break

# Write a Program to make quiz for Kaun Banega Crorepati.
class KBC():
    def __init__(self):
        print("Hello!!!Namaste".center(100));print()
        print("Welcome to KBC".center(100)) ;print()
    score=0
    correct_count=0
    correct_ans={}
    incorrect_ans={}
    def que_bank(self):
        Q1="Que-1) Where is an ocean with no water?"
        Q2="Que-2) What is always coming,but never arrives?"
        Q3="Que-3) If you have a bowl with six apples and you take away four, how many do you have?"
        Q4="Que-4) Some months have 31 days, others have 30 days, but how many have 28 days?"
        Q5="Que-5) What is it that goes up, but never comes down?"
        Q6="Que-6) The present age of Aradhana and Aadrika is in the ratio 3:4. 5 years back,the ratio of their ages was 2:3. What is the present age of Aradhana?"
        Q7="Que-7) A train running at the speed of 15.55 m/s crosses a pole in 18 seconds. What is the length of the train?"
        Q8="Que-8) Introducing Neeta, Anil said, ‘She is the wife of my mother’s only son.’ How is Neeta related to Anil?"
        Q9="Que-9) A father is twice as old as his daughter. If 20 years ago, the age of the father was 10 times the age of the daughter, what is the present age of the father?"
        Q10="Que-10) If you divide 30 by half and add ten, what do you get?"

        self.que_option={
                Q1:("A) On Map","B) Dessert","C) On Earth","D) None"),
                Q2:("A) Today","B) Tomorrow","C) Next Day","D) Yesterday"),
                Q3:("A) 2","B) 3","C) 4","D) 6"),
                Q4:("A) 11","B) 5","C) 1","D) 12"),
                Q5:("A) Age","B) Stairs","C) Kite","D) Birds"),
                Q6:("A) 20","B) 15","C) 5","D) 10"),
                Q7:("A) 200","B) 250","C) 180","D) 150"),
                Q8:("A) Mother","B) Sister","C) Daughter-in-law","D) Wife"),
                Q9:("A) 45","B) 22","C) 42","D) 24"),
                Q10:("A) 35","B) 70","C) 50","D) None")
                }
            
        #dictionaries of correct options and their answer     
        self.ans_bank_value={Q1:"A) On Map",Q2:"B) Tomorrow",Q3:"C) 4",Q4:"D) 12",Q5:"A) Age",Q6:"B) 15",Q7:"C) 180",Q8:"D) Wife",Q9:"A) 45",Q10:"B) 70"}
        self.ans_bank={Q1:"A",Q2:"B",Q3:"C",Q4:"D",Q5:"A",Q6:"B",Q7:"C",Q8:"D",Q9:"A",Q10:"B"}

        for question in self.que_option:
            print(question)                                     #prints questions
            for option in self.que_option[question]:           #prints options
                print(option)
            print()
            KBC.answer_validation(self)

    def answer_validation(self):
        for k in self.ans_bank:
            self.answer=self.ans_bank[k]
            self.ans_bank.pop(k)                     #to remove dict item one by one,.pop() is used with break in for loop
            break
        user_ans=input("Enter Correct option: A/B/C/D: ").upper()          #to convert user ans into uppercase,str upper() method is used.
        if self.answer==user_ans:
            print("-->Correct Answer.")
            self.score+=50
            self.correct_count+=1
            KBC.list_correct(self)
            
        else:
            print("Incorrect Answer.")
            self.score-=20
            KBC.list_incorrect(self)
        print("Your Current Score is:",self.score)
        print("-----------------------------")
        
    def list_correct(self):
        for i in self.ans_bank_value:
            self.correct_ans[i]=self.ans_bank_value[i]  
            self.ans_bank_value.pop(i)  
            break     

    def list_incorrect(self):
        for i in self.ans_bank_value:
            self.incorrect_ans[i]=self.ans_bank_value[i]
            self.ans_bank_value.pop(i)  
            break  

    def view_list(self):
        status=True
        while status:
            print("Press 1 to view Correct answer List.\nPress 2 for Incorrect answer list.\nPress 3 for correct and incorrect both lists.")
            list_choice=int(input("Enter your choice:"));print();print()
            if list_choice==1:
                print("list of correct questions and answers are :")
                for i in self.correct_ans:
                    print(i,"\nCorrect Answer--->",self.correct_ans[i])
                    print()
            elif list_choice==2:
                print("list of incorrect questions are:")
                for i in self.incorrect_ans:
                    print(i,"\ninCorrect Answer--->",self.incorrect_ans[i])
                    print()
            elif list_choice==3:
                print("list of correct questions are:")
                for i in self.correct_ans:
                    print(i,"\nCorrect Answer--->",self.correct_ans[i]);print()
                print()
                print("list of incorrect questions are:");print()
                for i in self.incorrect_ans:
                    print(i,"\nCorrect Answer--->",self.incorrect_ans[i])
                    print()
            view_list_choice=(input("Press 'y' to continue and 'n' for exit: ")).lower()
            if view_list_choice=='n':
                status=False
                break

    def menu(self):
        print("Press 1 for Play the Game.\n Press 2 for quit the game.")
        choice=int(input("Enter your choice:"));print()
        if choice==1:
            print("**Instruction: You will get +50 points for each correct answer and -20 points for each wrong answer");print();input()
            KBC.que_bank(self)  
            print("Correct Answer=",self.correct_count,"out of 10")
            print("Quiz completed! Your Total Score out of 500 is:",self.score);print();print()
            KBC.view_list(self)
        elif choice==2:
            print("You have choosed to Quit Quiz.")
        else:
            print("Invalid choice")

class menu():
    def __init__(self):
        print("Welcome to game zone.".center(100))
        print("There are three games available in this game zone.\n1) Rock Paper Scissors\n2) Housie Game\n3) KBC Quiz");print()
    def display(self):
        print("Press 1 for 'RPS'. \nPress 2 for 'HG'.\nPress 3 for 'KBC'.")
        choice=int(input("Enter your choice :"))
        if choice==1:
            obj=RPS()
            obj.play_RPS(0,0)
        elif choice==2:
            obj_HG=HG()
            obj_HG.play_housie()
        elif choice==3:
            obj_KBC=KBC()
            obj_KBC.menu()
            # obj_KBC.question_bank()
            # obj_KBC.answer_validation()
            # obj_KBC.list_correct()
            # obj_KBC.list_incorrect()
            # obj_KBC.view_list()
        else:
            print("Invalid choice.")

status=True
obj_menu=menu()
while status:
    choice=input("-->Now if you want to play game then press 'y' or 'yes' and press 'n' or 'no' for exit this game zone.:")
    if choice=='y' or choice=='yes':
        obj_menu.display()
    elif choice=='n' or choice=='no':
        print("Bye Bye!!")
        status=False