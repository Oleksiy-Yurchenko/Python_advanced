import random


# 1) Write a function that emulates the game "rock, scissors, paper"
# At the entrance, your function accepts your version printed from the console, the computer makes a decision randomly.


def rock_scissors_paper():
    """Function emulates emulates the game "rock, scissors, paper. It takes user choice from console, validates it,
    generates computer's choice, evaluates and prints game result to console."""

    rock_scissors_paper = ['rock', 'scissors', 'paper']
    min_val = 1
    max_val = 3
    input_menu = '''
        Type 1 to select Rock
        Type 2 to select Scissors
        Type 3 to select Paper
        Type 0 to quit

        Enter your choice:
    '''
    welcome_message = 'Welcome to the game "rock, scissors, paper"!'
    error_message = '{0} is not a valid choice. Please enter 1, 2, 3 or 0.'
    bye_message = 'You quit the game. Thank you for using "rock, scissors, paper"!'
    draw_message = "Your choice - {0}, computer's choice - {1}. Draw, but you were very close to win:)"
    win_message = "Your choice - {0}, computer's choice - {1}. You win, Congrats!"
    lost_message = "Your choice - {0}, computer's choice - {1}. Sorry, you lost( try again."

    def get_humans_choice():
        """Function takes choice of user from console, validates it and returns integer of user's choice"""
        while True:
            humans_choice = input(input_menu)
            try:
                humans_choice = int(humans_choice)
                if not humans_choice:
                    break
                elif (humans_choice > max_val) or (humans_choice < min_val):
                    print(error_message.format(humans_choice))
                else:
                    break
            except ValueError:
                print(error_message.format(humans_choice))
        return humans_choice

    def evaluate_result(humans_choice, computer_choice):
        """Function evaluates game result."""
        game_eval = computer_choice - humans_choice
        if not game_eval:
            return generate_result_message(draw_message)
        elif game_eval == 1 or game_eval == -2:
            return generate_result_message(win_message)
        elif game_eval == 2 or game_eval == -1:
            return generate_result_message(lost_message)

    def generate_result_message(message):
        """Function generates and prints to the console result message."""
        return message.format(rock_scissors_paper[humans_choice], rock_scissors_paper[computer_choice])

    print(welcome_message)
    humans_choice = get_humans_choice()
    if not humans_choice:
        return bye_message
    humans_choice -= 1
    computer_choice = random.randrange(0, len(rock_scissors_paper), 1)
    return evaluate_result(humans_choice, computer_choice)


print(rock_scissors_paper())


# 2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days at any given time.
# Do you have enough toilet paper(TP) to make it through?
# Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
# and the average person uses 57 sheets per day.

# Create a function that will receive a dictionary with two key/values:
# "people" ⁠— Number of people in the household.
# "tp" ⁠— Number of rolls.
# Return a statement telling the user if they need to buy more TP!


def toilet_paper_endurance(input_dict):
    """Function takes as an argument a dictionary with 2 arguments, validates input, and evaluate toilet paper amount
    required for a given number of people for 14 days. """
    sheets = 500
    person_use_pday = 57
    tp_endurance = 14
    all_ok_message = "You're are fine for now!"
    panic_message = "Houston, we've got a problem! Your toilet paper endurance is below {0} days!"

    try:
        if not isinstance(input_dict, dict):
            raise TypeError
        if int(input_dict['tp']) * sheets >= int(input_dict['people']) * person_use_pday * tp_endurance:
            return all_ok_message
        return panic_message.format(tp_endurance)
    except TypeError:
        return 'Function expected a dictionary as an argument.'
    except KeyError:
        return 'Input must contain a dictionary with two key/values: "people" and "tp".'
    except ValueError:
        return 'Input dictionary values must be integers or string representation of integers.'


print(toilet_paper_endurance({'tp': 12, 'people': 4}))
print(toilet_paper_endurance({'tp': 1, 'people': 40}))
print(toilet_paper_endurance({'tp': 5, 'people': 8}))
print(toilet_paper_endurance([]))
print(toilet_paper_endurance({'np': 5, 'people': 8}))
print(toilet_paper_endurance({'tp': 12, 'people': 4}))
print(toilet_paper_endurance({'tp': 'Nil', 'people': 'Far too many'}))

# 3) Make a function that encrypts a given input with these steps:
# Input: "apple"
# Step 1: Reverse the input: "elppa"
# Step 2: Replace all vowels using the following chart:
# a => 0
# e => 1
# i => 2
# o => 2
# u => 3
# # "1lpp0"
# Example:
# encrypt("banana") ➞ "0n0n0baca"
# encrypt("karaca") ➞ "0c0r0kaca"
# encrypt("burak") ➞ "k0r3baca"
# encrypt("alpaca") ➞ "0c0pl0aca"


def encrypt(word):
    '''Function encrypts string input as follows: 1) Reverse input. 2) Replace all vowels using the following chart:
    a => 0, e => 1, i => 2, o => 2, u => 3'''

    vowels = {'a': '0', 'e': '1', 'i': '2', 'o': '2', 'u': '3'}

    def word_to_reversed_array(word):
        '''Function converts word to list and reverses it. Validates the input.'''
        array_word = list(word.lower())
        array_word.reverse()
        return array_word

    def vowels_to_digits(list_from_word, vowels_dict):
        '''Function changes elements in input list to corresponding key: values of the given dictionary.'''
        for i in range(len(list_from_word)):
            if array_word[i] in vowels_dict:
                list_from_word[i] = vowels_dict[list_from_word[i]]

    try:
        if not isinstance(word, str):
            raise TypeError
    except TypeError:
        return '{0} must be a string'.format(word)
    else:
        array_word = word_to_reversed_array(word)
        vowels_to_digits(array_word, vowels)
        return ''.join(array_word)


print(encrypt('banana'), ' ➞ 0n0n0b')
print(encrypt('karaca'), ' ➞ 0c0r0k')
print(encrypt('burak'), ' ➞ k0r3b')
print(encrypt('alpaca'), ' ➞ 0c0pl0')


# **4)Given a 3x3 matrix of a completed tic-tac-toe game, create a function that returns whether the game is a win
# for "X", "O", or a "Draw", where "X" and "O" represent themselves on the matrix, and "E" represents an empty spot.
# Example:
# tic_tac_toe([
#     ["X", "O", "X"],
#     ["O", "X", "O"],
#     ["O", "X", "X"]
# ]) ➞ "X"
#
# tic_tac_toe([
#     ["O", "O", "O"],
#     ["O", "X", "X"],
#     ["E", "X", "X"]
# ]) ➞ "O"
#
# tic_tac_toe([
#     ["X", "X", "O"],
#     ["O", "O", "X"],
#     ["X", "X", "O"]
# ]) ➞ "Draw"


def tic_tac_toe(matrix):
    """Function takes 3 x 3 matrix as an argument with 'X', 'O' or 'E' elements. Function represents Tic Tac Toe Game
    and returns 'X' or 'O' or 'Draw'. Function validates the input matrix."""

    def assess_xoe_array(xoe_array):
        """Function assesses input array containing 'X', 'O' or 'E' and returns an array element if all array elements
        are same (for 'X' or 'O'). Function return 'Draw' if array contains 'E' element or anu combination of 'X' and
        'O' elements."""

        if ('E' in xoe_array) or ('O' in xoe_array and 'X' in xoe_array):
            return 'Draw'
        return xoe_array[0]

    def create_all_matrix_arrays(matrix):
        """Function generates and returns an array of all arrays from matrix, 3 arrays from rows, 3 arrays from columns,
        an array from main diagonal and an array from anti diagonal."""

        range_len_matrix = range(len(matrix))
        main_diag = [matrix[i][i] for i in range_len_matrix]
        anti_diag = [matrix[i][len(matrix) - 1 - i] for i in range_len_matrix]
        rows = matrix
        columns = [[row[i] for row in matrix] for i in range_len_matrix]
        return [main_diag] + [anti_diag] + rows + columns

    try:
        if not isinstance(matrix, list):
            raise TypeError
        if len(matrix) != 3:
            raise ValueError
        for row in matrix:
            if not isinstance(row, list):
                raise TypeError
            if len(row) != 3:
                raise ValueError
    except TypeError:
        return 'Matrix must be a list of lists.'
    except ValueError:
        return 'Matrix must be a 3 x 3 matrix.'
    else:
        all_matrix_arrays = create_all_matrix_arrays(matrix)
        results_array = list(filter(lambda array: assess_xoe_array(array) != 'Draw', all_matrix_arrays))
        return results_array[0] if len(results_array) == 1 else 'Draw'


print(tic_tac_toe([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]]), ' ➞ X')
print(tic_tac_toe([["O", "O", "O"], ["O", "X", "X"], ["E", "X", "X"]]), ' ➞ O')
print(tic_tac_toe([["X", "X", "O"], ["O", "O", "X"], ["X", "X", "O"]]), ' ➞ Draw')
print(tic_tac_toe([["X", "X", "O"], ["X", "O", "O"], ["X", "X", "O"]]), ' ➞ Draw')
print(tic_tac_toe([[], [], []]), ' ➞ Matrix must be a 3 x 3 matrix.')
print(tic_tac_toe([["X", "X", "O", "X", "X", "O"], ["X", "X", "O"], []]), ' ➞ Matrix must be a 3 x 3 matrix.')
print(tic_tac_toe([["X", "X", "O"], ["X", "X", "O"]]), ' ➞ Matrix must be a 3 x 3 matrix.')
print(tic_tac_toe(()), ' ➞ Matrix must be a list of lists.')
print(tic_tac_toe([("X", "X", "O"), ["X", "X", "O"], ["X", "X", "O"]]), ' ➞ Matrix must be a list of lists.')
print(tic_tac_toe('word'), ' ➞ Matrix must be a list of lists.')
