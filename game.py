
def __index_increase(index_list: list) -> list:
    return [[(x + 1, y + 1) for x, y in inner_list] for inner_list in index_list]


def __solve(matrix: list, word: str) -> list:
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

    return word_indices


def solver(board: list, words: list) -> dict:
    ordered_indices = {}
    for word in words:
        solution = __index_increase(__solve(board, word.upper()))
        if word not in ordered_indices:
            ordered_indices[word] = solution
        else:
            ordered_indices[word].append(solution)

    return ordered_indices
