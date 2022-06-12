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

if want_difficulty == "easy":
    print("You chose easy")

if want_difficulty == "medium":
    print("You chose medium")

if want_difficulty == "hard":
    print("You chose hard")
