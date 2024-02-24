import os
from glob import glob
from typing import Union


def get_input_path(puzzles_base_path: str) -> Union[dict, None]:
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
    content = []
    for k in solved_indices:
        content.append(f'{k}:\t\t{solved_indices[k]}')

    solution_path = os.path.join(puzzle_input_path, 'solution.txt')
    with open(solution_path, 'w') as f:
        f.write('\n'.join(content))
