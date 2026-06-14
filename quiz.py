score = 0

print("Welcome to the General Knowledge Quiz!\n")

answer = input("1. What is the capital of France? ")

if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Paris.")

answer = input("\n2. What is the largest planet in our solar system? ")

if answer.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is Jupiter.")

answer = input("\n3. What is the chemical symbol for water? ")

if answer.lower() == "h2o":
    print("Correct!")
    score += 1
else:
    print("Wrong! The answer is H2O.")

print("\nQuiz Complete!")
print("Your final score is:", score, "/3")
