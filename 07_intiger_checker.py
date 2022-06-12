def int_check(question):

    situation = ""



    while True:

        try:
            response = int(input(question))


        # checks input is a integer 
        except ValueError:
            print("Please enter an integer")
            continue
        