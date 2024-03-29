import os
from game import solver
from arrange_puzzles import get_input_path, create_puzzle_solution


def get_board(board_text_file_path: str) -> list:
    """
    This function reads a text file from the provided path and returns a list of lines in the file.

    :param board_text_file_path: A string representing the path to the text file.

    :return: A list of strings where each string is a line from the text file.
    """
    with open(board_text_file_path, 'r') as f:
        file = f.read()
    lines = file.split('\n')
    return lines


def get_words(words_file_path: str) -> list:
    """
    This function reads a text file from the provided path and returns a list of lines in the file.

    :param words_file_path: A string representing the path to the text file.

    :return: A list of strings where each string is a line from the text file.
    """
    with open(words_file_path, 'r') as f:
        file = f.read()
    lines = file.split('\n')
    return lines


if __name__ == '__main__':
    puzzles_base_path = os.path.join(os.getcwd(), 'puzzles')

    puzzles = get_input_path(puzzles_base_path)

    for puzzle in puzzles:
        puzzle_, words_ = puzzles[puzzle]
        puzzle_path = puzzles[puzzle][puzzle_]
        words_path = puzzles[puzzle][words_]

        board = get_board(puzzle_path)
        words = get_words(words_path)

        solved_board = solver(board, words)

        puzzle_directory = os.sep.join(puzzle_path.split(os.sep)[:-1])
        create_puzzle_solution(puzzle_input_path=puzzle_directory, solved_indices=solved_board)
