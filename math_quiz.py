import random

def generate_random_integer(min_value, max_value):
    """Generate a random integer between min_value and max_value."""
    return random.randint(min_value, max_value)

def choose_random_operation():
    """Randomly choose a mathematical operation: '+', '-', or '*'."""
    return random.choice(['+', '-', '*'])

def generate_math_problem():
    """Generate random numbers and an operation."""
    number1 = generate_random_integer(1, 10)
    number2 = generate_random_integer(1, 5)
    operation = choose_random_operation()
    return number1, number2, operation

def calculate_answer(number1, number2, operation):
    """Calculate the correct answer."""
    if operation == '+':
        return number1 + number2
    elif operation == '-':
        return number1 - number2
    else:
        return number1 * number2

def get_user_input():
    """Get user input for the answer, ensuring it is a valid integer."""
    while True:
        try:
            return int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def math_quiz():
    """Conduct a math quiz game and display the final score."""
    score = 0
    total_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questions):
        # Generate a math problem
        num1, num2, op = generate_math_problem()

        # Calculate the correct answer
        problem = f"{num1} {op} {num2}"
        answer = calculate_answer(num1, num2, op)
        print(f"\nQuestion: {problem}")

        # Get user input for the answer
        user_answer = get_user_input()

        # Check if the user's answer is correct
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
