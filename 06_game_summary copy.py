# If 'yes' show game history

game_summary = []

questions_correct = 0
questions_wrong = 0
questions_played = 0


# Show game statistics
# **** Calculate Game Stats ******
percent_correct = (questions_correct / questions_played) * 100
percent_wrong = (questions_wrong / questions_played) * 100

print()
print("***** Game History *******")
for game in game_summary:
        print(game)

print()

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
