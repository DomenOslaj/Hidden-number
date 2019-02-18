secret = 7

guess = raw_input("Which number do i have in mind? :) ")

guess = int(guess)

if guess == secret:
    print ("Congratulations, that is the right number!")

else:
    print ("Nope, try again! :)")