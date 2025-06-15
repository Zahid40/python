questions = [
    {
        "question": "Kaun Banega Crorepati is a game show based on which of the following?",
        "options": ["General Knowledge", "Mathematics", "Science", "History"],
        "answer": "General Knowledge",
        "price": 100000,
    },
    {
        "question": "Who is the host of Kaun Banega Crorepati?",
        "options": ["Amitabh Bachchan", "Shah Rukh Khan", "Salman Khan", "Aamir Khan"],
        "answer": "Amitabh Bachchan",
        "price": 1000000,
    },
    {
        "question": "What is the highest prize money in Kaun Banega Crorepati?",
        "options": ["1 crore", "7 crore", "10 crore", "50 lakh"],
        "answer": "7 crore",
        "price": 5000000,
    },
    {
        "question": "In which year did Kaun Banega Crorepati first air?",
        "options": ["2000", "2001", "2002", "1999"],
        "answer": "2000",
        "price": 10000000,
    },
    {
        "question": "Which of these is a lifeline used in Kaun Banega Crorepati?",
        "options": ["Phone a Friend", "Ask the Audience", "50:50", "All of the above"],
        "answer": "All of the above",
        "price": 70000000,
    },
]

user = {
    "name": "",
    "money": 0,
    "current_question": 0,
}


def start_game():
    print("Welcome to kaun banega crorepati!")
    user["name"] = input("Enter your name : ")
    print(f"Hello {user['name']}! Let's start the game.")
    user["money"] = 0
    user["current_question"] = 0
    user["lifelines_used"] = {
        "phone_a_friend": False,
        "ask_the_audience": False,
        "fifty_fifty": False,
    }
    for question in questions:
        print(f"\nQuestion {user['current_question'] + 1}: {question['question']}\n")
        for idx in range(len(question["options"])):
            print(f"{["A", "B", "C", "D"][idx]} - {question["options"][idx]}\n")

        answer = input("Your answer (A/B/C/D) : ").strip().lower()
        if answer in ["a", "b", "c", "d"]:
            selected_option = question["options"][["a", "b", "c", "d"].index(answer)]
            if selected_option == question["answer"]:
                user["money"] += question["price"]
                print(f"Correct! You have won {question['price']} and your total money is now {user['money']}.")
                user["current_question"] += 1
            else:
                print(f"Wrong answer! The correct answer was {question['answer']}.")
                print(f"You leave with {user['money']}.")
                break
        else:
            print("Invalid option. Please try again.")
            continue


start_game()
