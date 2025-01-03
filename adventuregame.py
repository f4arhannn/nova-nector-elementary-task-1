def play_game():
    name = input("What is your name? ")
    print("Hello, " + name + "! Welcome to the adventure game!")
    print("You are in a dark room and you have to choose between two doors. Choose wisely!")
    door = input("Which door do you choose? (black door or white door) ")

    if door == "black door":
        print("You have entered the treasure room. But you have to solve a riddle to get the treasure.")
        print("Riddle: What has keys but can't open locks?")
        answer = input("Enter your answer: ")
        if answer.lower() == "keyboard":
            print("Congratulations! You have got the treasure.")
        else:
            print("Sorry! Wrong answer. You missed the treasure.")
    elif door == "white door":
        print("You have entered the room of a fire-breathing dragon.")
        print("The dragon is sleeping. You have two choices: sneak past the dragon or fight the dragon.")
        choice = input("What do you choose? (sneak/fight) ")
        if choice == "sneak":
            print("You successfully sneaked past the dragon and found an exit. You are safe!")
        elif choice == "fight":
            print("You tried to fight the dragon but it woke up and burned you. Game over!")
        else:
            print("Invalid choice. The dragon woke up and burned you. Game over!")
    else:
        print("Invalid choice. You got stuck in the room forever. Game over!")

    print("Thank you for playing the adventure game!")

while True:
    play_game()
    play_again = input("Do you want to play again? (yes/no) ")
    if play_again.lower() != "yes":
        break