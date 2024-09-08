# phishing_quiz.py
def phishing_quiz():
    print("Welcome to the Phishing Awareness Quiz!")
    print("Answer the questions to see if you can spot the phishing attempt.\n")

    score = 0

    # Question 1
    print("1. You receive an email asking for your password to verify your account. What do you do?")
    print("A) Send the password immediately.")
    print("B) Report the email to IT.")
    answer1 = input("Your answer: ").strip().upper()
    if answer1 == "B":
        score += 1
        print("Correct!\n")
    else:
        print("Wrong! Never send your password via email.\n")

    # Question 2
    print("2. The email says 'Urgent! Your account has been locked, click here to unlock'. What should you check?")
    print("A) The link's URL by hovering over it.")
    print("B) Click the link to unlock.")
    answer2 = input("Your answer: ").strip().upper()
    if answer2 == "A":
        score += 1
        print("Correct!\n")
    else:
        print("Wrong! Always verify URLs before clicking.\n")

    print(f"Quiz Complete! Your score: {score}/2")
    
if __name__ == "__main__":
    phishing_quiz()
