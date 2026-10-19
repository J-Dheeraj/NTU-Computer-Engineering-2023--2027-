from password import getStrongPassword

users = {
    "Test": "Test12345",
    "Jack": "Test12345",
    "Tom": "Password1"
}

def getUserChoice():
    return int(input('''Please select one of the following options:
 1. User registration
 2. User Login
 3. Play the game as a guest\n'''))

def userRegistration():
    username = input("Input your user name: ")
    while username in users:
        print("The user exists. Please choose another user name.")
        username = input("Input your user name: ")
    password = getStrongPassword()
    users[username] = password
    print("New User registered. You can start the game.")

def userLogin():
    username = input("Input user name: ")
    if username not in users:
        print("Username does not exist!")
        return
    password = input("Input password: ")
    
    if users.get(username) == password:
        print(f"Welcome back, {username}, You can start the game.")
    else:
        print("Invalid password!")

def chooseQuiz():
    return int(input('''Dear Guest, you have to pass one quiz to play the game.
 Please select one of the following quizzes:
 1. Number guessing
 2. Calculate sum\n'''))

def guessingNumber():
    import random
    number = random.randint(1, 9)
    trials = 0
    
    while True:
        trials += 1
        guess = int(input("Enter an integer from 1 to 9: "))
        if guess < number:
            print("Guess is low")
        elif guess > number:
            print("Guess is high")
        else:
            print(f"Congratulations. You guessed it by {trials} trials!")
            return True

def calculateSum():
    # Dummy implementation for the sum game
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    if num1 + num2 == int(input("Enter the sum: ")):
        print("Correct!")
        return True
    else:
        print("Wrong sum!")
        return False

def guestQuiz():
    quizChoice = chooseQuiz()
    if quizChoice == 1:
        if guessingNumber():
            print("Congratulations. You can start the game.")
    elif quizChoice == 2:
        if calculateSum():
            print("Congratulations. You can start the game.")

def main():
    choice = getUserChoice()
    if choice == 1:
        userRegistration()
    elif choice == 2:
        userLogin()
    elif choice == 3:
        guestQuiz()

if __name__ == "__main__":
    main()
