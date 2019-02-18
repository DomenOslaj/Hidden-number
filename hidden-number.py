secret = 7

while True:
    guess = raw_input("Which number do i have in mind? :) ")

    guess = int(guess)

    if guess == secret:
        print ("Congratulations, that is the right number!")
        break

    else:
        print ("Nope, try again! :)")