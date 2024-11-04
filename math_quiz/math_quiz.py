import random


def random_integer(min: int, max: int) -> int:
    """
    Generates a random integer N with minimum <= N <= maximum.

    Args:
    min (int): The minimum value of N.
    max (int): The maximum value of N.

    Returns:
    int: A random integer N with minimum <= N <= maximum.

    Examples:
    >>> random_integer(1, 10)
    7
    >>> random_integer(3, 5)
    3
    """
    return random.randint(min, max)


def random_operator() -> str:
    """
    Randomly selects an arithmetic operator: '+', '-', or '*'.

    Returns:
    str: A randomly selected arithmetic operator.

    Examples:
    >>> random_operator()
    '+'
    >>> random_operator()
    '*'
    """
    return random.choice(['+', '-', '*'])


def arithmetic_operation(operand_1: int, operand_2: int,
                         operator: str) -> tuple[int, str]:
    """
    Performs an arithmetic operation on two operands.

    Args:
    operand_1 (int): The first operand.
    operand_2 (int): The second operand.
    operator (str): The arithmetic operator.

    Returns:
    int: The result of the arithmetic operation.
    str: The arithmetic operation.

    Examples:
    >>> arithmetic_operation(3, 5, '+')
    ('3 + 5', 8)
    >>> arithmetic_operation(7, 2, '-')
    ('7 - 2', 5)
    """
    operation = f"{operand_1} {operator} {operand_2}"
    if operator == '+':
        result = operand_1 + operand_2
    elif operator == '-':
        result = operand_1 - operand_2
    elif operator == '*':
        result = operand_1 * operand_2
    else:
        raise ValueError("Invalid operator")
    return operation, result


def math_quiz() -> None:
    """
    Creates a math quiz where the user is presented with randomly
    generated arithmetic operationsand needs to provide the correct
    answers. The user inputs the answer, and the game checks if the answer is
    correct and gives feedback to the user. At the end of the game, the user's total
    score is displayed.

    Returns:
        None
        
    """
    # Initialize the score and number of questions
    score = 0
    number_of_questions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, "
          "and you need to provide the correct answers.")

    # Loop through the number of questions
    for _ in range(number_of_questions):
        # Generate random operands and operator
        operand_1 = random_integer(1, 10)
        operand_2 = random_integer(1, 5)
        operator = random_operator()

        # Perform and print the arithmetic operation
        problem, answer = arithmetic_operation(operand_1, operand_2, operator)
        print(f"\nQuestion: {problem}")

        # Get the answer from the user
        user_answer = input("Your answer: ")
        user_answer = int(user_answer)
        
        # Check if the answer is correct
        if user_answer == answer:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    # Print the final score
    print(f"\nGame over! Your score is: {score}/{number_of_questions}")


if __name__ == "__main__":
    math_quiz()
