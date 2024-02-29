
def __remove_duplicate_lists(input_list: list) -> list:
    """
    This function takes a list of lists as input, sorts each sublist, and removes any duplicates.
    It returns a list of the unique sorted sublists.
    """
    unique_lists = []
    for sublist in input_list:
        sorted_sublist = sorted(sublist)
        if sorted_sublist not in unique_lists:
            unique_lists.append(sorted_sublist)
    return unique_lists


def __index_increase(index_list: list) -> list:
    """
    This function takes a list of lists as input, where each inner list contains tuples of two integers.
    It increases each integer in each tuple by 1.
    It returns a list of lists with the updated tuples.
    """
    return [[(x + 1, y + 1) for x, y in inner_list] for inner_list in index_list]


def __solve(matrix: list, word: str) -> list:
    """
    This function takes a 2D list (matrix) and a string (word) as input.
    It searches for the word in the matrix horizontally, vertically, and diagonally (both forward and backward).
    It returns a list of lists, where each inner list contains the indices of the letters of the word in the matrix.
    """
    word_indices = []
    rows, cols = len(matrix), len(matrix[0])

    # Remove spaces from the word
    word = word.replace(" ", "")

    # Check horizontally
    for i in range(rows):
        for j in range(cols - len(word) + 1):
            if matrix[i][j:j+len(word)].replace(" ", "") == word or \
               matrix[i][j:j+len(word)].replace(" ", "")[::-1] == word:
                word_indices.append([(i, k) for k in range(j, j+len(word))])

    # Check vertically
    for i in range(cols):
        for j in range(rows - len(word) + 1):
            if [matrix[k][i] for k in range(j, j+len(word))] == list(word) or \
               [matrix[k][i] for k in range(j, j+len(word))][::-1] == list(word):
                word_indices.append([(k, i) for k in range(j, j+len(word))])

    # Check diagonally (forward)
    for i in range(rows - len(word) + 1):
        for j in range(cols - len(word) + 1):
            if [matrix[i+k][j+k] for k in range(len(word))] == list(word) or \
               [matrix[i+k][j+k] for k in range(len(word))][::-1] == list(word):
                word_indices.append([(i+k, j+k) for k in range(len(word))])

    # Check diagonally (backward)
    for i in range(len(word)-1, rows):
        for j in range(cols - len(word) + 1):
            if [matrix[i-k][j+k] for k in range(len(word))] == list(word) or \
               [matrix[i-k][j+k] for k in range(len(word))][::-1] == list(word):
                word_indices.append([(i-k, j+k) for k in range(len(word))])

    # Check reverse diagonally (forward)
    for i in range(len(word)-1, rows):
        for j in range(len(word)-1, cols):
            if [matrix[i-k][j-k] for k in range(len(word))] == list(word) or \
               [matrix[i-k][j-k] for k in range(len(word))][::-1] == list(word):
                word_indices.append([(i-k, j-k) for k in range(len(word))])

    # Check reverse diagonally (backward)
    for i in range(rows - len(word) + 1):
        for j in range(cols - len(word) + 1):
            if [matrix[i+k][j-k] for k in range(len(word))] == list(word) or \
               [matrix[i+k][j-k] for k in range(len(word))][::-1] == list(word):
                word_indices.append([(i+k, j-k) for k in range(len(word))])

    return __remove_duplicate_lists(word_indices)


def solver(board: list, words: list) -> dict:
    """
    This function takes a 2D list (board) and a list of strings (words) as input.
    It finds the indices of each word in the board using the __solve function and increases each index by 1 using the __index_increase function.
    It returns a dictionary where the keys are the words and the values are the lists of indices.
    """
    ordered_indices = {}
    for word in words:
        solution = __index_increase(__solve(board, word.upper()))
        if word not in ordered_indices:
            ordered_indices[word] = solution
        else:
            ordered_indices[word].append(solution)

    return ordered_indices
