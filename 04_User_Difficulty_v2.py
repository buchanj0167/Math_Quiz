import random

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

    #Randomly generates maths questions with number between 0 and 10
    #Operator is randomly picked out of (+,)
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
            score+=1
        else:
            print("You're Wrong!")
    #Outputs the users score
    print("You got "+str(score)+" right!")

score =0

if want_difficulty =="medium":

    #medium MODE
    #Sets score to 0

    #initialises dictionary
    questions = {}

    #Randomly generates maths questions with number between 0 and 10
    #Operator is randomly picked out of (+,)
    for i in range(10):
        int_a = random.randint(100,200)
        int_b = random.randint(100,200)
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
            score+=1
        else:
            print("You're Wrong!")
    #Outputs the users score
    print("You got "+str(score)+" right!")




score =0

if want_difficulty =="hard":

    #medium MODE
    #Sets score to 0

    #initialises dictionary
    questions = {}

    #Randomly generates maths questions with number between 0 and 10
    #Operator is randomly picked out of (+,)
    for i in range(10):
        int_a = random.randint(500,1000)
        int_b = random.randint(500,1000)
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
            score+=1
        else:
            print("You're Wrong!")
    #Outputs the users score
    print("You got "+str(score)+" right!")