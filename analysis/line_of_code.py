def get_lines_of_code(filepath):
    lineno = 0
    with open(filepath) as f:
        lineno = sum(1 for _ in f)
    return lineno