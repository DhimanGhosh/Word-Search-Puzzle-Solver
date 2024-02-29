import os
from glob import glob
from typing import Union


def get_input_path(puzzles_base_path: str) -> Union[dict, None]:
    """
    This function takes a base path for puzzles as input, and returns a dictionary mapping
    each puzzle directory to the paths of its corresponding puzzle and words files.
    If any puzzle directory does not contain both a puzzle.txt and words.txt file,
    the function returns None.

    :param puzzles_base_path: A string representing the base path of the puzzles.
    :return: A dictionary with puzzle directory names as keys and another dictionary as values,
             which contains `puzzle` and `words` as keys mapped to their respective file paths.
             Returns None if any puzzle or words file is missing in any of the puzzle directories.
    """
    puzzles_directories = glob(os.path.join(puzzles_base_path, f'puzzle*'))
    puzzles_path = {}
    if puzzles_directories:
        for puzzle_directory in puzzles_directories:
            puzzle_path = glob(os.path.join(puzzle_directory, 'puzzle.txt'))
            words_path = glob(os.path.join(puzzle_directory, 'words.txt'))
            if not puzzle_path or not words_path:
                return None
            puzzles_path[puzzle_directory.split(os.sep)[-1]] = {'puzzle': puzzle_path[0], 'words': words_path[0]}
    return puzzles_path


def create_puzzle_solution(puzzle_input_path: str, solved_indices: dict) -> None:
    """
    This function creates a solution for a puzzle and writes it to a text file.

    Parameters:
    puzzle_input_path (str): The path where the solution file will be created.
    solved_indices (dict): A dictionary containing the solved indices of the puzzle.

    Returns: None
    """
    content = []
    for k in solved_indices:
        content.append(f'{k}:\t\t{solved_indices[k]}')

    solution_path = os.path.join(puzzle_input_path, 'solution.txt')
    with open(solution_path, 'w') as f:
        f.write('\n'.join(content))
