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
        print("You will be asked how many rounds you would like to play on that difficulty.")
        print()
        print("Then you will be givin 10 random questions based on your difficulty.")
        print()
        print("GOOD LUCK :)")
        print()
        return""
        
yes_no_list = ["yes","no"]
yes_no_error = "Please answer yes or no"

want_instructions = choice_checker("Do you want to see the instructions? ",yes_no_list, yes_no_error)

if want_instructions == "yes":
    instructions()

print()

