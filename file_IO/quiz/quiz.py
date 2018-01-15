def show_menu():
    print("1. Ask questions")
    print("2. Add a question")
    print("3. Exit Game")

    option = input("Enter option: ")
    return option

def add_question():
    print("")
    question = input("Enter a question\n> ")

    print("")
    print("OK then, tell me the answer")
    answer = input("{0}\n> ".format(question))

    file = open("questions.txt", "a")
    file.write(question + "\n")
    file.write(answer + "\n")
    file.close()

def ask_questions():
    questions = []
    answers = []

    file = open("questions.txt", "r")
    lines = file.read().splitlines()
    lines = enumerate(lines)

    for i, text in lines:
        if i%2 == 0:
            questions.append(text)
        else:
            answers.append(text)

    file.close()

    number_of_questions = len(questions)
    questions_and_answers = zip(questions, answers)

    score = 0

    for question, answer in questions_and_answers:
        guess = input(question + "> ")
        print(len(guess))
        print(len(answer))
        if guess == answer:
            score += 1
            print("right")
            print(score)
        else:
            print("wrong")


    print ("You got {0} correct out of {1}".format(score, number_of_questions))

def game_loop():
    while True:
        option = show_menu()
        if option == "1":
            ask_questions()
            print("You selected 'Ask questions'")
        elif option == "2":
            add_question()
            print("You selected 'Add a question'")
        elif option == "3":
            break
        else:
            print("Invalid Option")
        print("")

game_loop()