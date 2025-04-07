#Quiz game
# This is a simple quiz game that asks the user questions about the capitals of different countries.

print("Welcome to the quiz game!")
score = 0
playing = input('Do you want to play?  ')
if playing.lower() != 'yes':
    quit()
print('Great! Let\'s play!') 

answer = input('What is the capital of France?  ')
if answer.lower() == 'paris':
    print('Correct!')
    score += 1
    print('Your score is ' + str(score))
else:
    print('Incorrect! The correct answer is Paris.')
answer = input('What is the capital of Germany?  ')
if answer.lower() == 'berlin':
    print('Correct!')
    score += 1
    print('Your score is ' + str(score))
else:
    print('Incorrect! The correct answer is Berlin.')

answer = input('What is the capital of Italy?  ')
if answer.lower() == 'rome':
    print('Correct!')
    score += 1
    print('Your score is ' + str(score))
else:
    print('Incorrect! The correct answer is Rome.')
answer = input('What is the capital of Spain?  ')
if answer.lower() == 'madrid':
    print('Correct!')
    score += 1
    print('Your score is ' + str(score))
else:
    print('Incorrect! The correct answer is Madrid.')
    
answer = input('What is the capital of Portugal?  ')
if answer.lower() == 'lisbon':
    print('Correct!')
    score += 1
    print('Your score is ' + str(score))    
else:
    print('Incorrect! The correct answer is Lisbon.')

print('You got  ' + str(score) + " quetion correct")
print('You got '+ str((score/4)*100) + '%')
print('Thanks for playing!')