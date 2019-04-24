import random


def main():
    secret = random.randint(1, 30)

    while True:
        guess = raw_input("Which number do i have in mind? :) ")

        guess = int(guess)

        if guess == secret:
            print ("Congratulations, that is the right number!")
            break

        elif guess > secret:
            print ("Nope, try something smaller! :)")

        elif guess < secret:
            print ("Nope, try something bigger! :)")

if __name__ == "__main__":  # this means that if somebody ran this Python file, execute only the code below
    main()