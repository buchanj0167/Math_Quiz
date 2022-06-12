def int_check(question, low=0, high=10000):

        situation = ""

        if low is not 0 and high is not 10000:
            situation = "both"
        elif low is not 0 and high is 10000:
            situation = "low only"

        while True:

            try:
                response = int(input(question))

                # checks input is not too high or too low if a both upper and lower bounds are specified
                if situation == "both":
                    if response < low or response > high:
                        print("Please enter a valid integer".format(low, high))
                        continue
                # checks input is not too low
                elif situation == "low only":
                    if response < low:
                        print("Please enter a valid integer".format(low))
                        continue
                return response

            # checks input is a integer 
            except ValueError:
                print("Please enter an integer")
                continue