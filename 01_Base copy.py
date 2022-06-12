import random
from urllib import response

def int_check(question, low=0, high=10000):

    situation = ""

    if low is not None and high is not None:
        situation = "both"
    elif low is not None and high is None:
        situation = "low only"

    while True:

        try:
            response = int(input(question))

            # checks input is not too high or too low if a both upper and lower bounds are specified
            if situation == "both":
                if response < 0 or response > 10000:
                    print("Please enter a number between {} and {}".format(low, high))
                    continue

        # checks input is a integer 
        except ValueError:
            print("Please enter an integer")
            continue
        return response 





def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # interates through list and if response is an item
        # in the list (or the first letter of an item), the full item 
        # name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()


def instructions():
        print()
        print("You will be asked what difficulty you would like to play with Easy, Medium, Hard.")
        print()
        print("Then you will be givin 10 random questions based on your difficulty.")
        print()
        print("GOOD LUCK :)")
        print()
        return""

# integer checker
# makes sure user inputs a number



        
yes_no_list = ["yes","no"]
yes_no_error = "Please answer yes or no"

want_instructions = choice_checker("Do you want to see the instructions? ",yes_no_list, yes_no_error)

if want_instructions == "yes":
    instructions()

print()

def choice_checker(question, valid_list, error):

    valid = False
    while not valid:

        # Ask user for choice (and put choice in lowercase)
        response = input(question).lower()

        # interates through list and if response is an item
        # in the list (or the first letter of an item), the full item 
        # name is returned

        for item in valid_list:
            if response == item[0] or response == item:
                return item

        # output error if item not in list
        print(error)
        print()

        
easy_medium_hard_list = ["easy","medium","hard"]
easy_medium_hard_error = "Please answer easy, medium or hard"

want_difficulty = choice_checker("what difficulty would you like? ",easy_medium_hard_list, easy_medium_hard_error)




score=0

if want_difficulty == "easy":
#Easy MODE
#Sets score to 0



#initialises dictionary
    questions = {}
    game_summary = []
    questions_correct = 0
    questions_wrong = 0
    questions_played = 0

    #Randomly generates maths questions with number between 0 and 10
    #Operator is randomly picked out of (+)
    for i in range(10):
        int_a = random.randint(0,10)
        int_b = random.randint(0,10)
        operators = ['+']
        operator_value = random.choice(operators)
        question = str(int_a)+" "+operator_value+" "+str(int_b)
        answer = str(eval(question))
        question+=": "
    
    
        #adds the question to questions dictionary
        questions.update({question:answer})

    #Iterates through the questions in the dictionary and response respectively
    for q in questions.keys():
        user_answer=input(q)
        if questions.get(q)==user_answer:
            print("Correct!")
            feedback = "correct"
            score+=1
            questions_correct+=1
        else:
            print("You're Wrong!")
            feedback = "incorrect"
            questions_wrong+=1
    #Outputs the users score
    print("You got "+str(score)+" right!")



score =0

if want_difficulty == "medium":
#Medium MODE
#Sets score to 0

#initialises dictionary
    questions = {}
    game_summary = []
    questions_correct = 0
    questions_wrong = 0
    questions_played = 0

    #Randomly generates maths questions with number between 0 and 10
    #Operator is randomly picked out of (+)
    for i in range(10):
        int_a = random.randint(50,100)
        int_b = random.randint(50,100)
        operators = ['+']
        operator_value = random.choice(operators)
        question = str(int_a)+" "+operator_value+" "+str(int_b)
        answer = str(eval(question))
        question+=": "
    
        #adds the question to questions dictionary
        questions.update({question:answer})

    #Iterates through the questions in the dictionary and response respectively
    for q in questions.keys():
        user_answer=input(q)
        if questions.get(q)==user_answer:
            print("Correct!")
            feedback = "correct"
            score+=1
            questions_correct+=1
        else:
            print("You're Wrong!")
            feedback = "incorrect"
            questions_wrong+=1
    #Outputs the users score
    print("You got "+str(score)+" right!")





score =0
if want_difficulty == "hard":
#HARD MODE
#Sets score to 0

#initialises dictionary
    questions = {}
    game_summary = []
    questions_correct = 0
    questions_wrong = 0
    questions_played = 0

    #Randomly generates maths questions with number between 0 and 10
    #Operator is randomly picked out of (+)
    for i in range(10):
        int_a = random.randint(200,600)
        int_b = random.randint(200,600)
        operators = ['+']
        operator_value = random.choice(operators)
        question = str(int_a)+" "+operator_value+" "+str(int_b)
        answer = str(eval(question))
        question+=": "
    
        #adds the question to questions dictionary
        questions.update({question:answer})

    #Iterates through the questions in the dictionary and response respectively
    for q in questions.keys():
        user_answer=input(q)
        if questions.get(q)==user_answer:
            print("Correct!")
            feedback = "correct"
            score+=1
            questions_correct+=1
            
        else:
            print("You're Wrong!")
            feedback = "incorrect"
            questions_wrong+=1
    #Outputs the users score
    print("You got "+str(score)+" right!")

    outcome = "Round {}: {}".format(questions_played, feedback)

    game_summary.append(outcome)


    

print()
user_history = choice_checker("Would you like to see your game history? ", yes_no_list, yes_no_error)
if user_history == "yes":



# If 'yes' show game history
    questions_played += 1
    outcome = "Question {}: {}".format(questions_played, feedback)








# Show game statistics
# **** Calculate Game Stats ******
percent_correct = (questions_correct / questions_played) * 10
percent_wrong = (questions_wrong / questions_played) * 10



    # displays game stats with % values to the nearest whole number
print("******* Quiz Statistics *******")
print("Correct: {}, ({:.0f}%) ".format(questions_correct, percent_correct))
print("Incorrect: {}, ({:.0f}%) ".format(questions_wrong, percent_wrong))
            

    # End of Game Statements 
print()
print('***** End Quiz Summary *****')
print("Correct: {} \t|\t Incorrect:{} ".format(questions_correct, questions_wrong))

print()
print("***** Thanks for playing *****")

